# src/ingest.py
import argparse
import pandas as pd
from sqlalchemy import text
from db import get_engine
import os
import json # Importe a biblioteca json

def main(csv_path):
    df = pd.read_csv(csv_path)

    # Renomear colunas do seu CSV
    df = df.rename(columns={
        'room_id/id': 'device_id',
        'noted_date': 'reading_timestamp',
        'temp': 'temperature',
        'out/in': 'location'
    })

    # Garantir tipos corretos
    df['reading_timestamp'] = pd.to_datetime(df['reading_timestamp'], errors='coerce')

    # Manter payload extra (out/in)
    # Converta o dicionário em uma string JSON
    df['raw_payload'] = df[['location']].apply(lambda row: json.dumps(row.dropna().to_dict()), axis=1)

    # Selecionar colunas finais
    df = df[['device_id', 'temperature', 'reading_timestamp', 'raw_payload']]

    engine = get_engine()

    # Criar tabela caso não exista
    init_sql = open(os.path.join('sql', 'init_table.sql')).read()
    with engine.begin() as conn:
        conn.execute(text(init_sql))

    # Inserir dados no banco
    df.to_sql('temperature_readings', engine, if_exists='append', index=False, method='multi')
    print(f'✅ Inseridos {len(df)} registros em temperature_readings')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--csv', required=True, help='Caminho do CSV (ex: data/IOT-temp.csv)')
    args = parser.parse_args()
    main(args.csv)