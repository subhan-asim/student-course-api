from app import crud, models
from fastapi import APIRouter, HTTPException, status, Query, Depends
from app.routes.auths import get_current_user

router = APIRouter(prefix="/students", tags=["Students"])

@router.post('/new')
def create_student(student: models.Student, current_user = Depends(get_current_user)):
    _ = crud.add_student(student.name)
    if _ == True:
        return {"info":f"Successfully Added {student.name} to students.", "status_code": 201}
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Student Already Exists.")


@router.delete('/delete')
def delete_student(student: models.Student, current_user = Depends(get_current_user)):
    _ = crud.remove_student(student.name)
    if _ == True:
        return {"info":f"Successfully removed {student.name} from students.", "status_code": 201}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not fonund.")


@router.post('/enrollments/new')
def enroll_student(info: models.Enrollment):
    _ = crud.enroll(info.s_name, info.c_name)
    if _ == True:
        return {"info":f"Successfully enrolled {info.s_name} in {info.c_name}.", "status_code": 201}
    elif _ == "404":
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student or Course is invalid.")
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Student Already enrolled in this course.")
@router.get('/info')
def s_info(
    name: str | None = Query(None, description="Filter by student name."),
    page: int = Query(1, ge=1, description="Page Number"),
    limit: int = Query(10, ge=1, description="Results per page")
):
    _ = crud.view_students_with_courses(name, page, limit)
    return {"page": page,
            "limit": limit,
            "result": _}


