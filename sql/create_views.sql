-- View: Média de temperatura por dispositivo (com nome da coluna ajustado)
CREATE OR REPLACE VIEW avg_temp_por_dispositivo AS
SELECT device_id AS room_id, AVG(temperature) AS avg_temperature
FROM temperature_readings
GROUP BY device_id;

-- View: Leituras por hora
CREATE OR REPLACE VIEW leituras_por_hora AS
SELECT EXTRACT(HOUR FROM reading_timestamp) AS hora, COUNT(*) AS total_leituras
FROM temperature_readings
GROUP BY hora
ORDER BY hora;

-- View: Temperatura máxima e mínima por dia
CREATE OR REPLACE VIEW temp_max_min_por_dia AS
SELECT DATE(reading_timestamp) AS dia,
       MAX(temperature) AS temp_maxima,
       MIN(temperature) AS temp_minima
FROM temperature_readings
GROUP BY dia
ORDER BY dia;