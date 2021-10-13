from fastapi import FastAPI
from services2 import read_file, sum_mark, group_based_student, sort_based_sum
app = FastAPI()


data1 = read_file()


@app.get("/list")
async def get_list():
    return {
        "code": 200,
        "result": data1
    }

sum1 = sum_mark(data1)


@app.get("/list/student_mark")
async def get_list_mark():
    return {
        "code": 200,
        "result": sum1
    }

group = group_based_student(data1)


@app.get("/list/student_subjects")
async def get_list_subject():
    return {
        "code": 200,
        "result": group
    }

sort = sort_based_sum()


@app.get("/list/student_sort_sum_mark")
async def get_list_sort_mark():
    return {
        "code": 200,
        "result": sort
    }

