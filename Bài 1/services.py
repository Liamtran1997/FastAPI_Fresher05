

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


def sort_list(student_id: str):

    try:

        result = list(filter(lambda student: student['id'] == student_id, studentdb))[0]
        return result

    except Exception as ex:

        print(str(ex))


