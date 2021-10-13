from typing import Optional
from fastapi import FastAPI
from schemas import Student
from services import studentdb, sort_list

app = FastAPI()


@app.get("/students")
async def get_list():
    return {
        "code": 200,
        "result": studentdb
    }


@app.get("/students/{student_id}")
async def get_student(student_id: str):
    result = sort_list(student_id)
    return {
        "code": 200,
        "result": result
    }


@app.post("/students/create")
async def add_student(student: Student):
    studentdb.append(student.dict())
    return {
        "code": 200,
        "result": studentdb
    }


@app.put("/students/update/{student_id}", response_model=Student)
async def update_student(student_id: str, student: Student):

    try:
        target_std = sort_list(student_id)
        target_std["id"] = student.id
        target_std["name"] = student.name
        target_std["address"] = student.address
        target_std["email"] = student.email
        return {
            "code": 200,
            "result": studentdb
        }

    except Exception as ex:

        print(str(ex))
        return {
            "code": 400,
            "result": "student not found"

        }


@app.delete("/students/{student_id}")
def delete_student(student_id: str):

    try:
        result = sort_list(student_id)
        studentdb.remove(result)
        return {
            "code": 200,
            "result": studentdb
        }
    except Exception as ex:

        print(str(ex))
        return {
                "code": 400,
                "result": studentdb
                }



