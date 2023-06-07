DROP TABLE IF EXISTS pokemon;

CREATE TABLE pokemon (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    name VARCHAR(20) NOT NULL,
    hp INTEGER NOT NULL,
    attack INTEGER NOT NULL,
    defense INTEGER NOT NULL,
    speed INTEGER NOT NULL,
    sp_attack INTEGER,
    sp_defense INTEGER,
    desc VARCHAR(60),
    image BLOB
);