from database.database import conectar

def listar_tarefas(user_id):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM tarefas WHERE user_id = ?",(user_id,))

    tarefas = cursor.fetchall()
    conexao.close()
    return tarefas

def criar_tarefa(titulo, prioridade, user_id):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""INSERT INTO tarefas (titulo, prioridade, user_id)
                    VALUES(?, ?, ?)""", 
                    (titulo, prioridade, user_id)) 

    conexao.commit()
    conexao.close()

def concluir_tarefa(id):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("UPDATE tarefas SET status = 1 WHERE id = ?",(id,))

    conexao.commit()
    conexao.close()

def excluir_tarefa(id):
    conexao = conectar()
    cursor = conexao.cursor()
    
    cursor.execute("DELETE FROM tarefas WHERE id = ?", (id,))

    conexao.commit()
    conexao.close()