CREATE TABLE POKEMON_MAP (
    encounter_id    DOUBLE PRECISION,
    pokemon_id      INT,
    expire          DOUBLE PRECISION,
    latitude        DOUBLE PRECISION,
    longitude       DOUBLE PRECISION,
    PRIMARY KEY (encounter_id)
);

CREATE INDEX pokemon_id_idx ON POKEMON_MAP(pokemon_id);
CREATE INDEX expire_idx ON POKEMON_MAP(expire);
CREATE INDEX latitude_idx ON POKEMON_MAP(latitude);
CREATE INDEX longitude_idx ON POKEMON_MAP(longitude);
