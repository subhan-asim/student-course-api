from app import crud, models
from fastapi import APIRouter, HTTPException, status, Query, Depends
from app.routes.auths import get_current_user

router = APIRouter(prefix="/courses", tags=["Courses"])

@router.post('/new')
def create_course(course: models.Course):
    _ = crud.add_course(course.name, current_user = Depends(get_current_user))
    if _ == True:
        return {"info":f"Successfully Added {course.name} to Courses.", "status_code":201}
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Course Already Exists.")
    
@router.delete('/delete')
def delete_course(course: models.Course, current_user = Depends(get_current_user)):
    _ = crud.remove_course(course.name)
    if _ == True:
        return {"info":f"Successfully removed {course.name} from courses.", "status_code":201}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No such course found")
    
@router.get('/info')
def c_info(
    name: str | None = Query(None, description="Filter by student name."),
    page: int = Query(1, ge=1, description="Page Number"),
    limit: int = Query(10, ge=1, description="Results per page")
):
    _ = crud.view_courses_with_students(name, page, limit)
    return {"page": page,
            "limit": limit,
            "result": _}
