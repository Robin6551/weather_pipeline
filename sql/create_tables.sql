CREATE TABLE IF NOT EXISTS dim_location(
    location_id SERIAL PRIMARY KEY,
    city TEXT NOT NULL,
    country TEXT NOT NULL,
    latitude NUMERIC,
    longitude NUMERIC,
    UNIQUE(city, country)
);

CREATE TABLE IF NOT EXISTS fact_weather (
    weather_id SERIAL PRIMARY KEY,
    location_id INT NOT NULL REFERENCES dim_location(location_id),
    observed_at TIMESTAMP NOT NULL,
    temperature NUMERIC,
    humidity INT,
    pressure INT,
    weather_main TEXT,
    weather_description TEXT,
    ingestion_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)

CREATE INDEX IF NOT EXISTS idx_fact_weather_observed_at
ON fact_weather(observed_at)

CREATE INDEX IF NOT EXISTS idx_fact_weather_location
ON fact_weather(location_id)