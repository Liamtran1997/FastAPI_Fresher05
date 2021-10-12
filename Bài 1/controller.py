from typing import Optional
from fastapi import FastAPI
from schemas import Student
from fastapi.encoders import jsonable_encoder

app = FastAPI()
studentdb = [
        {
            "id": "S01",
            "name": "nguyen minh anh",
            "address": {
                "street": "Dong Da",
                "city": "Ha Noi",
                "country": "Viet Nam"
            },
            "email": "Steven0011@gmail.com"
        }, {
            "id": "S02",
            "name": "dang thanh minh",
            "address": {
                "street": "Mai Lao Bang",
                "city": "Da Nang",
                "country": "Viet Nam"
            },
            "email": "Mike123@gmail.com"
        }, {
            "id": "S03",
            "name": "hoang duc tuan",
            "address": {
                "street": "Hai Ho",
                "city": "Da Nang",
                "country": "Viet Nam"
            },
            "email": "Tuan54321@gmail.com"
        }, {
            "id": "S04",
            "name": "tran duc hung",
            "address": {
                "street": "Dang Thai Mai",
                "city": "Ho Chi Minh City",
                "country": "Viet Nam"
            },
            "email": "Tommmm@gmail.com"
        }, {
            "id": "S05",
            "name": "vu hoang thanh",
            "address": {
                "street": "Hai Ba Trung",
                "city": "Ha Noi",
                "country": "Viet Nam"
            },
            "email": "KrutCobain@gmail.com"
        }
    ]


@app.get("/students")
async def get_list():
    return {
        "code": 200,
        "result": studentdb
    }


@app.get("/students/{student_id}")
async def get_student(student_id: str):
    result = list(filter(lambda student: student['id'] == student_id, studentdb))
    return {
        "code": 200,
        "result": result[0] if result else {}
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
        target_std = list(filter(lambda std: std["id"] == student_id, studentdb))[0]
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
    return {
        "code": 200,
        "result": studentdb

    }


@app.delete("/students/{student_id}")
def delete_student(student_id: str):

    try:
        result = list(filter(lambda student: student['id'] == student_id, studentdb))[0]
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
            return {
                "code": 200,
                "result": studentdb

            }
