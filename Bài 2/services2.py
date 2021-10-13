import csv


def read_file():
    data1 = []
    try:
        with open('student.csv') as CsvFile:
            CsvReader = csv.DictReader(CsvFile)
            for row in CsvReader:
                data1.append(row)
        return data1
    except Exception:
        print("Error!!!")


def init_dict(**kargs):
    return {
        "id": kargs["id"],
        "name": kargs["name"],
        "sum_mark": kargs["sum_mark"]
    }


def sum_mark(lst):
    list_rs = []
    set_id = set([sv['id'] for sv in lst])
    for ele in set_id:
        lsv_msv = list(filter(lambda e: e['id'] == ele, lst))
        sum_diem = sum(int(item['mark']) for item in lsv_msv)
        dict_temp = init_dict(id=ele, name=lsv_msv[0]['name'], sum_mark=sum_diem)
        list_rs.append(dict_temp)
    return list_rs


def group_based_student(lst):
    data1 = {}
    for item in lst:
        if item['id'] not in data1:
            data1.update({
                item['id']: {
                    'id': item['id'],
                    'name': item['name'],
                    'subjects': [{"subject": item['subject'], "mark":item['mark']}]
                }
            })
        else:
            data1[item['id']]['subjects'].append({"subject": item['subject'], "mark": item['mark']})
    return data1


data1 = read_file()
sum1 = sum_mark(data1)


def sort_based_sum():
    sort_sum = sorted(sum1, key=lambda x: x["sum_mark"], reverse=True)
    return sort_sum





