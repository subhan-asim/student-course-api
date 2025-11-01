from app.db import get_connection
import sqlite3

conn = get_connection()

# --- STUDENT FUNCTIONS ---


def register_user(user, password) -> bool:
    conn = get_connection()
    try:
        c = conn.cursor()
        c.execute("INSERT INTO users(username, password) VALUES (?, ?)", (user, password))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()



def add_student(s_name: str) -> bool:
    conn = get_connection()
    try:
        c = conn.cursor()
        name = s_name.strip()
        c.execute("INSERT INTO students (name) VALUES (?)", (name,))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()


def remove_student(s_name: str) -> bool:
    conn = get_connection()
    try:
        c = conn.cursor()
        name = s_name.strip()
        c.execute("SELECT id FROM students WHERE name = ?", (name,))
        student = c.fetchone()

        if not student:
            return False

        student_id = student[0]
        c.execute("DELETE FROM enrollments WHERE student_id = ?", (student_id,))
        c.execute("DELETE FROM students WHERE id = ?", (student_id,))
        conn.commit()
        return True
    finally:
        conn.close()


# --- COURSE FUNCTIONS ---

def add_course(c_name: str) -> bool:
    conn = get_connection()
    try:
        c = conn.cursor()
        name = c_name.strip()
        c.execute("INSERT INTO courses (name) VALUES (?)", (name,))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()


def remove_course(c_name: str) -> bool:
    conn = get_connection()
    try:
        c = conn.cursor()
        name = c_name.strip()
        c.execute("SELECT id FROM courses WHERE name = ?", (name,))
        course = c.fetchone()

        if not course:
            return False

        course_id = course[0]
        c.execute("DELETE FROM enrollments WHERE course_id = ?", (course_id,))
        c.execute("DELETE FROM courses WHERE id = ?", (course_id,))
        conn.commit()
        return True
    finally:
        conn.close()


# --- ENROLLMENTS ---

def enroll(student_name: str, course_name: str) -> bool:
    conn = get_connection()
    try:
        c = conn.cursor()
        s_name = student_name.strip()
        c_name = course_name.strip()

        # Fetch IDs
        c.execute("SELECT id FROM students WHERE name = ?", (s_name,))
        student = c.fetchone()
        c.execute("SELECT id FROM courses WHERE name = ?", (c_name,))
        course = c.fetchone()

        if not student or not course:
            return "404"

        try:
            c.execute(
                "INSERT INTO enrollments (student_id, course_id) VALUES (?, ?)",
                (student[0], course[0]),
            )
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False
    finally:
        conn.close()


# --- VIEW FUNCTIONS ---

def view_students_with_courses(name: str = None, page: int = 1, limit: int = 10):
    result = []
    conn = get_connection()
    try:
        c = conn.cursor()
        offset = (page - 1) * limit
        query = """
            SELECT students.name AS student_name, courses.name AS course_name
            FROM students
            LEFT JOIN enrollments ON students.id = enrollments.student_id
            LEFT JOIN courses ON enrollments.course_id = courses.id
            WHERE (? IS NULL OR students.name LIKE ?)
            ORDER BY students.name ASC
            LIMIT ? OFFSET ?;
                """
        name_filter = f"%{name}%" if name else None
        c.execute(query, (name_filter, name_filter, limit, offset))
        rows = c.fetchall()

        if not rows:
            return [{"Result": "No students found"}]

        for student, course in rows:
            result.append({
                "student": student,
                "course": course or "Not Enrolled"
            })
        return result
    finally:
        conn.close()


def view_courses_with_students(name: str = None, page: int = 1, limit: int = 10):
    result = []
    conn = get_connection()
    offset = (page - 1) * limit
    try:
        c = conn.cursor()
        query = """
            SELECT courses.name, students.name
            FROM courses
            LEFT JOIN enrollments ON courses.id = enrollments.course_id
            LEFT JOIN students ON enrollments.student_id = students.id
            WHERE (? IS NULL OR courses.name LIKE ?)
            ORDER BY courses.name ASC
            LIMIT ? OFFSET ?
                """
        name_filter = f"%{name}%"
        c.execute(query, (name_filter, name_filter, limit, offset))
        rows = c.fetchall()

        if not rows:
            return [{"Result": "No courses found"}]

        for course, student in rows:
            result.append({
                "course": course,
                "student": student or "No students enrolled"
            })
        return result
    finally:
        conn.close()
