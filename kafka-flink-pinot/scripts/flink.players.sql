CREATE TABLE Players
(
    player_id             INT,
    player_name           STRING,
    player_country        STRING,
    player_age            INT,
    player_created_time   TIMESTAMP(3)
) WITH (
      'connector' = 'kafka',
      'topic' = 'players',
      'properties.bootstrap.servers' = 'kafka:9092',
      'scan.startup.mode' = 'earliest-offset',
      'format' = 'json'
      );

SELECT *
FROM PLayers
WHERE LOWER(player_name) LIKE '%emma%';

CREATE TABLE Games
(
    game_id             INT,
    game_name           STRING,
    game_created_time   TIMESTAMP(3)
) WITH (
      'connector' = 'kafka',
      'topic' = 'games',
      'properties.bootstrap.servers' = 'kafka:9092',
      'scan.startup.mode' = 'earliest-offset',
      'format' = 'json'
      );

SELECT * FROM Games
WHERE LOWER(game_name) LIKE '%rush%';

CREATE TABLE PlayerScores
(
    player_id             INT,
    game_id               INT,
    score                 INT,
    score_time            TIMESTAMP(3)
) WITH (
      'connector' = 'kafka',
      'topic' = 'player_scores',
      'properties.bootstrap.servers' = 'kafka:9092',
      'scan.startup.mode' = 'earliest-offset',
      'format' = 'json'
      );

SELECT player_id, game_id, AVG(score) as avgScore
FROM PlayerScores
GROUP BY player_id, game_id;

CREATE TABLE PlayerScoresEnhanced
(
    player_id     INT,
    player_name   STRING, 
    game_id       INT,
    game_name     STRING,
    score         INT,
    score_time    TIMESTAMP(3),  
    PRIMARY KEY (player_id, game_id) NOT ENFORCED -- Declare the PRIMARY KEY constraint
) WITH (
      'connector' = 'upsert-kafka', -- This enables updates and deletes
      'topic' = 'player_scores_enhanced',
      'properties.bootstrap.servers' = 'kafka:9092',
      'key.format' = 'json', -- Key format is JSON, matching the value format
      'value.format' = 'json' -- Values are serialized in JSON
      );

INSERT INTO PlayerScoresEnhanced
    SELECT p.player_id,
           p.player_name,
           g.game_id,
           g.game_name,
           ps.score,
           ps.score_time
FROM PlayerScores ps
         JOIN
     Players p
     ON ps.player_id = p.player_id
         JOIN
     Games g
     ON ps.game_id = g.game_id;

SELECT player_name, game_name, AVG(score) as avgScore
FROM PlayerScoresEnhanced
GROUP BY player_name, game_name;