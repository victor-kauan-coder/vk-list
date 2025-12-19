# 📝 VK List – Gerenciador de Tarefas

O **VK List** é uma aplicação web de gerenciamento de tarefas desenvolvida com **Django 6.0**.  
O projeto utiliza uma interface moderna e responsiva baseada em **Bootstrap 5**, permitindo que usuários organizem suas rotinas com facilidade.

---

## 🚀 Funcionalidades

O sistema oferece um **ciclo completo de gerenciamento de tarefas (CRUD)**:

- **Listagem Ordenada**  
  Exibe todas as tarefas, ordenadas automaticamente pelo prazo de entrega mais próximo.

- **Criação e Edição**  
  Formulários validados para inserção e atualização de títulos e prazos.

- **Conclusão Inteligente**  
  Botão que registra automaticamente a data atual como data de finalização, desabilitando edições posteriores para manter o histórico.

- **Exclusão Segura**  
  Interface de confirmação que evita a remoção acidental de dados importantes.

---

## 🛠️ Tecnologias Utilizadas

### Backend
- **Framework:** Django 6.0  
- **Configuração de Ambiente:** Python-decouple  
- **Banco de Dados:** dj-database-url (SQLite por padrão)  
- **Formatação de Código:** Black 25.12.0  

### Frontend
- **Estilização:** Bootstrap 5.3  
- **Ícones:** Bootstrap Icons  
- **Internacionalização:**  
  - Idioma: Português Brasileiro (pt-br)  
  - Fuso horário: America/Fortaleza  

---

## 🔧 Configuração e Instalação

### Pré-requisitos
- Python 3.10 ou superior  
- Ambiente virtual (venv)

### Passos para execução

```bash
git clone https://github.com/victor-kauan-coder/vk-list.git
cd vk-list
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Arquivo .env

```env
SECRET_KEY=sua-chave-secreta-django
DEBUG=True
ALLOWED_HOSTS=127.0.0.1, localhost
```

---

## 📂 Estrutura de Rotas

- `/` – Lista principal de tarefas  
- `/create/` – Formulário de nova tarefa  
- `/update/<id>` – Edição de uma tarefa específica  
- `/delete/<id>` – Confirmação de exclusão  
- `/complete/<id>` – Marcar tarefa como concluída  
