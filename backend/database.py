import os
import psycopg2

def create_database():
    try:
        conn = psycopg2.connect(
            host="database",  # Nome do serviço no docker-compose.yml
            database=os.environ.get("POSTGRES_DB"),
            user=os.environ.get("POSTGRES_USER"),
            password=os.environ.get("POSTGRES_PASSWORD")
        )
        cur = conn.cursor()

        # Exemplo: Criar tabela (adapte ao seu esquema)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS minha_tabela (
                id SERIAL PRIMARY KEY,
                nome VARCHAR(255)
            )
        """)

        conn.commit()
        conn.close()
        print("Conexão com o PostgreSQL bem-sucedida!")

    except psycopg2.Error as e:
        print(f"Erro ao conectar com o PostgreSQL: {e}")
        raise  # Re-lança a exceção para ser tratada em app.py