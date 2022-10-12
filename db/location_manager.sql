DROP TABLE IF EXISTS cities;
DROP TABLE IF EXISTS countries;

CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    description TEXT,
    visit BOOLEAN
);

CREATE TABLE cities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    visit BOOLEAN,
    country_id INT NOT NULL REFERENCES countries (id)
)