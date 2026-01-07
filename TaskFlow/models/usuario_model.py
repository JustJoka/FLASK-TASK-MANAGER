from database.database import conectar

def cadastrar_usuario(nome, email, senha):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)", (nome, email, senha))

    conexao.commit()
    conexao.close()

def buscar_usuario(email):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM usuarios WHERE email = ?",(email,)) 

    usuario = cursor.fetchone()
    conexao.close()
    return usuario

def autenticar_usuario(email, senha):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM usuarios WHERE email = ? AND senha = ?",(email, senha)) 

    return cursor.fetchone()