# 🎯 Online Quiz Application Using Django

## 📖 Project Overview

The **Online Quiz Application** is a Python Full Stack web application developed using **Django**, **HTML**, **CSS**, **JavaScript**, and **SQLite**. It provides an interactive platform where users can register, log in, attempt quizzes, and instantly view their scores along with the correct answers for incorrect responses.

The application includes a secure authentication system, an admin panel for managing quiz questions, and an attractive user interface, making it suitable for beginners learning Django and Python Full Stack Development.

---

# 📂 Project Architecture

```
ONLINE-QUIZ-APPLICATION/
│
├── onlinequiz/                  # Django Project
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   ├── wsgi.py
│   └── __init__.py
│
├── quiz/                        # Django Application
│   ├── migrations/
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   └── js/
│   │       └── script.js
│   │
│   ├── templates/
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── register.html
│   │   ├── login.html
│   │   ├── quiz.html
│   │   └── result.html
│   │
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── tests.py
│
├── db.sqlite3
├── manage.py
├── requirements.txt
├── README.md
└── venv/
```

---

# 🔧 Technologies Used

- 🐍 Python
- 🌐 Django
- 💻 HTML5
- 🎨 CSS3
- ⚡ JavaScript
- 🗄 SQLite Database
- 🔐 Django Authentication
- 📝 Django Forms

---

# ✨ Features

- 👤 User Registration
- 🔑 User Login & Logout
- 📝 Online Quiz
- 📊 Automatic Score Calculation
- ❌ Displays Wrong Answers
- ✅ Displays Correct Answers
- ⏱ Quiz Timer
- 📱 Responsive Design
- 📂 Django Admin Panel
- 🗄 SQLite Database

---

# 💫 Project Workflow

## User Registration

Users can create an account using the registration page.

---
## 📽️ Demo Video

Because of GitHub’s file size limitations, you can watch the full working demo of EduTutor AI here:

▶️ [Click to Watch the Demo on Google Drive](https://drive.google.com/file/d/1u5jTtzwd-0QCXPrCKPF8DLxT_IJOgQCI/view?usp=sharing)


----------------------

## User Login

Registered users can securely log in using Django Authentication.

---

## Start Quiz

After logging in, users can start the quiz.

Questions are fetched dynamically from the database.

---

## Submit Quiz

Users submit their answers.

The application compares user answers with the correct answers stored in the database.

---

## Result

The result page displays:

- Score
- Total Questions
- Wrong Answers
- Correct Answers
- Take Quiz Again Button

---

# 🗄 Database

SQLite Database stores

- Users
- Questions
- Quiz Results
- Sessions

---

# 🔐 Authentication

The project uses Django's built-in authentication system.

- Register
- Login
- Logout
- Session Management

---

# 🚀 How to Run the Project

## Clone Repository

```bash
git clone https://github.com/yourusername/online-quiz-application.git

cd online-quiz-application
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install django
```

or

```bash
pip install -r requirements.txt
```

---

## Apply Migrations

```bash
python manage.py makemigrations

python manage.py migrate
```

---

## Create Super User

```bash
python manage.py createsuperuser
```

---

## Run Server

```bash
python manage.py runserver
```

Open Browser

```
http://127.0.0.1:8000/
```

Admin Panel

```
http://127.0.0.1:8000/admin/
```

---

# 📽 Demo Video

Because GitHub has upload limitations, the complete demo video is available here.

▶️ Click Here to Watch Demo

(Add Google Drive Link)

---

# 📈 Future Enhancements

- Quiz Categories
- Leaderboard
- Quiz History
- Profile Page
- Email Verification
- Password Reset
- Certificate Generation
- Dark Mode

---

# 🤝 Contributions

Contributions are welcome.

Fork this repository

Create a new branch

Commit your changes

Push the branch

Create a Pull Request

---

# 📬 Contact

📧 Email: yourname@gmail.com

🐞 Issues: Open a GitHub Issue

---

# ⭐ Star This Repository

If you found this project useful, please give it a ⭐ on GitHub.

---

## 💼 Resume Description

Developed a **Python Full Stack Online Quiz Application** using **Django, HTML, CSS, JavaScript, and SQLite**. Implemented user authentication, dynamic quiz functionality, score calculation, quiz timer, wrong answer review, and Django Admin Panel for question management. Built using Django Forms, Models, Templates, and responsive front-end technologies.
