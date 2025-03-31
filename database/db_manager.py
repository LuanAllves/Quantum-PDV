import sqlite3
import re
import os
from tkinter import messagebox



# Verifica se a pasta existe e cria, se necessário
if not os.path.exists("database"):
    os.makedirs("database")

# Caminho completo para o banco de dados na pasta "database"
db_path = os.path.join("database", "pdv.db")

def conectar_banco():
    conexao = sqlite3.connect(db_path)
    return conexao

def salvar_dados(nome, email, telefone, endereco):
     # Banco de Dados: Criando ou conectando ao SQLite
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        telefone TEXT NOT NULL,
        endereco TEXT NOT NULL
    )
    """)

    # Salvar mudanças e fechar conexão
    conexao.commit()
    conexao.close()

    messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")




