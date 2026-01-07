🗂️ TaskFlow — Gerenciador de Tarefas com Flask

TaskFlow é um gerenciador de tarefas web desenvolvido com Flask, SQLite e Bootstrap, permitindo que usuários se cadastrem, façam login e gerenciem suas tarefas de forma simples e eficiente.
O projeto foi criado com foco em aprendizado prático de backend, organização em camadas (routes, models e database) e boas práticas para aplicações web.

🚀 Funcionalidades
)<br>
👤 Autenticação)<br>
Cadastro de usuários)<br>
Login com email e senha)<br>
Controle de sessão com Flask)<br>
Proteção de rotas (dashboard apenas para usuários logados))<br>
)<br>
✅ Tarefas
)<br>
Criar tarefas)<br>
Definir prioridade (Alta, Média, Baixa)<br>
Listar tarefas por usuário)<br>
Marcar tarefas como concluídas)<br>
Excluir tarefas)<br>
)<br>
🗄️ Banco de Dados)<br>
)<br>
SQLite)<br>
Relacionamento entre usuários e tarefas)<br>
Chaves estrangeiras ativadas (PRAGMA foreign_keys = ON))<br>
)<br>
🛠️ Tecnologias Utilizadas)<br>
)<br>
Python 3)<br>
Flask)<br>
SQLite)<br>
HTML5)<br>
CSS3)<br>
Bootstrap 5)<br>
Jinja2)<br>
)<br>
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

🔐 Fluxo da Aplicação)<br>
)<br>
Usuário acessa a página de login)<br>
Pode se registrar caso não tenha conta)<br>
Após login:)<br>
Sessão é criada)<br>
Usuário é redirecionado para o dashboard)<br>
)<br>
No dashboard:)<br>
Cria tarefas)<br>
Visualiza apenas suas próprias tarefas)<br>
Conclui ou exclui tarefas)<br>
)<br>
📸 Screenshots)<br>

![Preview](https://github.com/JustJoka/FLASK-TASK-MANAGER/blob/main/TaskFlow/static/images/Screenshot%202026-01-07%20144240.png?raw=true)
![Preview](https://github.com/JustJoka/FLASK-TASK-MANAGER/blob/main/TaskFlow/static/images/Screenshot%202026-01-07%20144245.png?raw=true)
![Preview](https://github.com/JustJoka/FLASK-TASK-MANAGER/blob/main/TaskFlow/static/images/Screenshot%202026-01-07%20144251.png?raw=true)
![Preview](https://github.com/JustJoka/FLASK-TASK-MANAGER/blob/main/TaskFlow/static/images/Screenshot%202026-01-07%20144310.png?raw=true)
![Preview](https://github.com/JustJoka/FLASK-TASK-MANAGER/blob/main/TaskFlow/static/images/Screenshot%202026-01-07%20144326.png?raw=true)
![Preview](https://github.com/JustJoka/FLASK-TASK-MANAGER/blob/main/TaskFlow/static/images/Screenshot%202026-01-07%20144337.png?raw=true)




