#!/bin/local/python

import json
import logging
import os
import random
import time

import numpy as np
import pandas as pd
from confluent_kafka import Producer


class Generator:
    def next(self) -> (str, object):
        pass

class PlayerDataGenerator(Generator):
    def __init__(self, df):
        self.df = df

    def next(self):
        for _, row in self.df.iterrows():
            key = str(row['player_id'])
            data = json.dumps(row.to_dict())
            yield key, data.encode('utf-8')

class GameDataGenerator(Generator):
    def __init__(self, df):
        self.df = df

    def next(self):
        for _, row in self.df.iterrows():
            key = str(row['game_id'])
            data = json.dumps(row.to_dict())
            yield key, data.encode('utf-8')

class ScoreGenerator(Generator):
    def __init__(self, df, df2):
        self.df = df
        self.df2 = df2

    def next(self):
        while True:
            key = random.randint(self.df['player_id'].min(), self.df['player_id'].max())
            game_id = random.randint(self.df2['game_id'].min(), self.df2['game_id'].max())
            # Generate a normally distributed score around 8 with standard deviation 1.5
            # Clip the score to ensure they stay within 0 to 10
            rating = np.random.normal(8, 1.5)
            rating = max(0, min(10, rating))  # Ensuring rating is between 0 and 10
            data = json.dumps({
                "player_id": key,
                "game_id": game_id,
                "score": round(rating, 2),
                "ratingTime": round(time.time() * 1000)
            })
            yield str(key).encode('utf-8'), data.encode('utf-8')

def read_jasonl(jsonl_file_path):
    stats = []
    try:
        with open(jsonl_file_path, 'r') as file:
            for line in file:
                # Parse each line as a JSON object
                record = json.loads(line.strip())
                stats.append(record)    
                print(f"Read {len(stats)} records from {jsonl_file_path}")

    except FileNotFoundError:
        print(f"Error: File '{jsonl_file_path}' not found")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in the file")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    
    return stats

def delivery_report(err, msg):
    """ Called once for each message produced to indicate a delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))


def send(p, topic, gen: Generator, limit: int = 100000):
    p.poll(0)
    count = 0

    for key, data in gen.next():
        while True:
            try:
                p.produce(
                    key=key,
                    topic=topic,
                    value=data,
                    on_delivery=delivery_report)
                break  # Break the loop if produce succeeds
            except BufferError:
                print('Local producer queue is full ({} messages awaiting delivery): trying again...'.format(len(p)))
                p.poll(1000)  # Wait a bit for the producer to clear up buffer space
        count += 1
        if count % 100 == 0:  # Adjust the frequency of poll() based on your application's requirement
            p.poll(0)  # Serve delivery callback queue
        if count >= limit:
            break

    # Wait for any outstanding messages to be delivered and delivery report
    # callbacks to be triggered.
    p.flush()


if __name__ == "__main__":
    bootstrap = os.getenv('BOOTSTRAPSERVER', 'kafka:9092')
    player_topic = os.getenv('PLAYER_TOPIC', 'players')
    game_topic = os.getenv('GAME_TOPIC', 'games')
    score_topic = os.getenv('SCORE_TOPIC', 'player_scores')
    lmt = int(os.getenv('LIMIT', 100000))
    gamepath = os.getenv('DATA', '/tmp/games.jsonl')
    playerpath = os.getenv('DATA2', '/tmp/players.jsonl')
    #if path is None:
    #    raise Exception("Need to players.jsonl and games.jsonl file")

    gamedf = pd.read_json(gamepath, lines=True)
    playerdf = pd.read_json(playerpath, lines=True)

    logging.basicConfig(level=logging.INFO)
    pr = Producer({'bootstrap.servers': bootstrap})


    player_gen = PlayerDataGenerator(playerdf)
    game_gen = GameDataGenerator(gamedf)
    score_gen = ScoreGenerator(playerdf, gamedf)

    # Send player data to player topic (no limit as we send all player)
    send(pr, topic=player_topic, gen=player_gen, limit=len(playerdf))

    # Send game data to game topic (no limit as we send all game)
    send(pr, topic=game_topic, gen=game_gen, limit=len(gamedf))

    # Continuously generate and send ratings data to ratings topic
    send(pr, topic=score_topic, gen=score_gen, limit=lmt)