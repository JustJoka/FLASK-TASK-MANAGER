import sqlite3
import os

def conectar():
    print("Banco em:", os.path.abspath("tasks.db"))
    conexao = sqlite3.connect("tasks.db")
    conexao.execute("PRAGMA foreign_keys = ON")
    return conexao


def tabela_usuarios():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                senha TEXT NOT NULL 
            )""")
    
    conexao.commit()
    conexao.close()

def tabela_tarefas():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS tarefas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                status INTEGER NOT NULL DEFAULT 0,
                prioridade TEXT NOT NULL,
                user_id INTEGER NOT NULL,
                FOREIGN KEY (user_id) REFERENCES usuarios (id)
            )""")
    
    conexao.commit()
    conexao.close()
