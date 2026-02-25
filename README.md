# 🎓 Student-Course Management API

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)  
![FastAPI](https://img.shields.io/badge/Framework-FastAPI-green.svg)  
![SQLite](https://img.shields.io/badge/Database-SQLite-blue.svg)  
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

FastAPI backend for managing students, courses, and enrollments — featuring secure JWT authentication, pagination, and SQLite storage. Built as a **portfolio project** to demonstrate backend and database proficiency.

---

# 📌 Overview

This API allows you to register and login users, add/remove students and courses, enroll students, and query enrollments with pagination and search. JWT authentication secures all endpoints. SQLite is used for data persistence, making it lightweight and easy to run locally.

---

# ⚙️ Features

- Register / Login with JWT Authentication  
- Add / Remove / List Students and Courses  
- Enroll Students into Courses  
- View all Enrollments with Pagination and Search  
- SQLite for persistence  
- Clean, modular FastAPI structure  

---

# 🏗 Tech Stack

- **FastAPI** – Backend Framework  
- **SQLite3** – Database  
- **JWT + Passlib** – Authentication  
- **Pydantic** – Data Validation  
- **Uvicorn** – ASGI Server  

---

# 🚀 Installation

### 1️⃣ Clone Repository

    git clone https://github.com/subhan-asim/student-course-api.git
    cd student-course-api

### 2️⃣ Create Virtual Environment

    python -m venv venv
    venv\Scripts\activate      # Windows
    source venv/bin/activate   # Mac/Linux

### 3️⃣ Install Dependencies

    pip install -r requirements.txt

### 4️⃣ Run the Server

    uvicorn app.main:app --reload

Server runs at `http://127.0.0.1:8000`

---

# 🔑 Authentication Flow

- Register a new user via `/auth/register`  
- Login via `/auth/login` to get a JWT token  
- Use `Authorization: Bearer <token>` header for all protected routes  

Supports CRUD operations with proper authentication.

---

# 📘 API Examples

| Method | Endpoint          | Description                     |
|--------|------------------------------|---------------------------------|
| POST   | /auth/register               | Register a new user             |
| POST   | /auth/login                  | Obtain JWT token                |
| POST   | /students/new                | Add a new student               |
| GET    | /students/info               | View all students               |
| POST   | /enrollments/enrollments/new | Enroll a student in a course    |

---

# 🖥 Console / API Preview

![Console Preview](images/console_preview.png)  
![API Preview](images/api_preview.png)

---

# 📜 License

MIT License © 2025 — Built for educational purposes