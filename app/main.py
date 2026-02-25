from fastapi import FastAPI
from app.routes import students, courses, auths

app = FastAPI(title="Student-Course API")

app.include_router(students.router)
app.include_router(courses.router)
app.include_router(auths.router)