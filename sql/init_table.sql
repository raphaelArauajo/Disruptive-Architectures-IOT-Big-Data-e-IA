CREATE TABLE IF NOT EXISTS temperature_readings (
    id SERIAL PRIMARY KEY,
    device_id VARCHAR(50),
    temperature FLOAT,
    reading_timestamp TIMESTAMP,
    raw_payload JSONB
);

