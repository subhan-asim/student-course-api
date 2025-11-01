# 🎓 Student-Course Management API

A FastAPI-based backend for managing students, courses, and enrollments — featuring secure JWT authentication, pagination, and SQLite storage.  
Built as a **portfolio project** to demonstrate backend and database proficiency.

---

## 🚀 Features
- Register / Login with JWT Authentication  
- Add / Remove / List Students and Courses  
- Enroll Students into Courses  
- View all Enrollments with Pagination and Search  
- SQLite for persistence  
- Clean, modular FastAPI structure  

---

## 🧰 Tech Stack
- **FastAPI** (Backend Framework)
- **SQLite3** (Database)
- **JWT + Passlib** (Authentication)
- **Pydantic** (Data Validation)
- **Uvicorn** (Server)

---

## ⚙️ Setup

### 1️⃣ Clone the repo
```bash
git clone https://github.com/<your-username>/student-course-api.git
cd student-course-api
2️⃣ Create virtual environment
bash
Copy code
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux
3️⃣ Install dependencies
bash
Copy code
pip install -r requirements.txt
4️⃣ Run the server
bash
Copy code
uvicorn app.main:app --reload
🔑 Authentication Flow
Register via /auth/register

Login via /auth/login → copy the token

Use Authorization: Bearer <token> for all other routes

Covers CRUD + Auth logic.

📘 API Examples
Method	Endpoint	Description
POST	/auth/register	Register a new user
POST	/auth/login	Obtain JWT token
POST	/students/	Add a new student
GET	/students/	View all students
POST	/enrollments/	Enroll student in a course

📜 License
MIT License © 2025 — Built for educational purposes.