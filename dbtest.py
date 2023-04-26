# pip install psycopg2

import psycopg2

# Instale a biblioteca psycopg2 usando: pip install psycopg2

def criar_conexao():
    conexao = psycopg2.connect(
        database="postgres",
        user="postgres",
        password="admin",
        host="127.0.0.1",
        port="5432"
    )
    return conexao

def criar_tabela(conexao):
    cursor = conexao.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS nomes (id SERIAL PRIMARY KEY, nome VARCHAR(255) NOT NULL);")
    conexao.commit()

def inserir_nome(conexao, nome):
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO nomes (nome) VALUES (%s);", (nome,))
    conexao.commit()

def exibir_nomes(conexao):
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM nomes;")
    nomes = cursor.fetchall()
    for nome in nomes:
        print(nome)

if __name__ == "__main__":
    conexao = criar_conexao()
    criar_tabela(conexao)
    inserir_nome(conexao, "João")
    exibir_nomes(conexao)
    conexao.close()
