from flask import render_template, Flask, request, redirect, session
from database.database import tabela_usuarios, tabela_tarefas
from models.usuario_model import autenticar_usuario, cadastrar_usuario, buscar_usuario
from models.tarefas_model import listar_tarefas, criar_tarefa, concluir_tarefa, excluir_tarefa

app = Flask(__name__)
app.secret_key = "chave_secreta"

tabela_usuarios()
tabela_tarefas()

@app.route("/", methods=["GET", "POST"])
def login():
    erro = None

    if request.method == "POST":
        email = request.form["email"]
        senha = request.form["senha"]

        usuario = autenticar_usuario(email, senha)
        if usuario:
            session["user_id"] = usuario[0]
            return redirect("/dashboard")
        else:
            erro = "Email ou senha inválidos"
    return render_template("login.html", erro=erro)

@app.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        senha = request.form["senha"]

        if buscar_usuario(email):
            return render_template("register.html", erro="Email já cadastrado!")

        cadastrar_usuario(nome, email, senha)
        return redirect("/")

    return render_template("register.html")

@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect("/")
    tarefas = listar_tarefas(session["user_id"])
    return render_template("dashboard.html", tarefas=tarefas)



@app.route("/nova-tarefa", methods=["POST"])
def nova_tarefa():
    if "user_id" not in session:
        return redirect("/")
    
    print("SESSION:", session)
    
    titulo = request.form["titulo"]
    prioridade = request.form["prioridade"]

    print("DADOS:", titulo, prioridade, session.get("user_id"))

    criar_tarefa(titulo, prioridade, session["user_id"])
    return redirect("/dashboard")



@app.route("/concluir/<int:id>")
def concluir(id):
    if "user_id" not in session:
        return redirect("/")
    
    concluir_tarefa(id)
    return redirect("/dashboard")



@app.route("/excluir/<int:id>")
def excluir(id):
    if "user_id" not in session:
        return redirect("/")
    
    excluir_tarefa(id)
    return redirect("/dashboard")


app.run(debug=True)