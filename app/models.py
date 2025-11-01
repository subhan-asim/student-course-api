from pydantic import BaseModel, Field

class Student(BaseModel):
    name: str = Field(..., strip_whitespace=True, min_length=2, max_length=30)

class Course(BaseModel):
    name: str = Field(..., strip_whitespace=True, min_length=2, max_length=30)

class Enrollment(BaseModel):
    s_name: str
    c_name: str
