# src/create_views.py
from db import get_engine
from sqlalchemy import text
import os

sql_path = os.path.join('sql','create_views.sql')
sql = open(sql_path).read()

def run():
    engine = get_engine()
    # split por ';' simples (suficiente para este arquivo)
    stmts = [s.strip() for s in sql.split(';') if s.strip()]
    with engine.begin() as conn:
        for s in stmts:
            conn.execute(text(s))

if __name__ == '__main__':
    run()
    print("Views criadas/atualizadas com sucesso.")
