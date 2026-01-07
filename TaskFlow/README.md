🗂️ TaskFlow — Gerenciador de Tarefas com Flask

TaskFlow é um gerenciador de tarefas web desenvolvido com Flask, SQLite e Bootstrap, permitindo que usuários se cadastrem, façam login e gerenciem suas tarefas de forma simples e eficiente.
O projeto foi criado com foco em aprendizado prático de backend, organização em camadas (routes, models e database) e boas práticas para aplicações web.

🚀 Funcionalidades

👤 Autenticação
Cadastro de usuários
Login com email e senha
Controle de sessão com Flask
Proteção de rotas (dashboard apenas para usuários logados)

✅ Tarefas

Criar tarefas
Definir prioridade (Alta, Média, Baixa)
Listar tarefas por usuário
Marcar tarefas como concluídas
Excluir tarefas

🗄️ Banco de Dados

SQLite
Relacionamento entre usuários e tarefas
Chaves estrangeiras ativadas (PRAGMA foreign_keys = ON)

🛠️ Tecnologias Utilizadas

Python 3
Flask
SQLite
HTML5
CSS3
Bootstrap 5
Jinja2

📂 Estrutura do Projeto
TaskFlow/<br>
│<br>
├── app.py<br>
│<br>
├── database/<br>
│   └── database.py<br>
│<br>
├── models/<br>
│   ├── usuario_model.py<br>
│   └── tarefas_model.py<br>
│<br>
├── templates/<br>
│   ├── login.html<br>
│   ├── register.html<br>
│   └── dashboard.html<br>
│<br>
├── static/<br>
│   ├── styles.css<br>
│   └── images/<br>
│       └── background.jpg<br>
│<br>
└── tasks.db<br>
<br>
⚙️ Como Executar o Projeto
1️⃣ Clone o repositório
git clone https://github.com/seu-usuario/taskflow.git
cd taskflow

2️⃣ Crie um ambiente virtual (opcional, recomendado)
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

3️⃣ Instale as dependências
pip install flask

4️⃣ Execute a aplicação
python app.py

5️⃣ Acesse no navegador
http://127.0.0.1:5000

🔐 Fluxo da Aplicação

Usuário acessa a página de login
Pode se registrar caso não tenha conta
Após login:
Sessão é criada
Usuário é redirecionado para o dashboard

No dashboard:
Cria tarefas
Visualiza apenas suas próprias tarefas
Conclui ou exclui tarefas

📸 Screenshots

![Preview](https://github.com/JustJoka/FLASK-TASK-MANAGER/blob/main/TaskFlow/static/images/Screenshot%202026-01-07%20144240.png?raw=true)
![Preview](https://github.com/JustJoka/FLASK-TASK-MANAGER/blob/main/TaskFlow/static/images/Screenshot%202026-01-07%20144245.png?raw=true)
![Preview](https://github.com/JustJoka/FLASK-TASK-MANAGER/blob/main/TaskFlow/static/images/Screenshot%202026-01-07%20144251.png?raw=true)
![Preview](https://github.com/JustJoka/FLASK-TASK-MANAGER/blob/main/TaskFlow/static/images/Screenshot%202026-01-07%20144310.png?raw=true)
![Preview](https://github.com/JustJoka/FLASK-TASK-MANAGER/blob/main/TaskFlow/static/images/Screenshot%202026-01-07%20144326.png?raw=true)
![Preview](https://github.com/JustJoka/FLASK-TASK-MANAGER/blob/main/TaskFlow/static/images/Screenshot%202026-01-07%20144337.png?raw=true)



