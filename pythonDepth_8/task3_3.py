# Напишите функцию, которая сохраняет созданный в
# прошлом задании файл в формате CSV.
import json
import csv


def json_to_csv(filename: str):
    with open(f'{filename}.json', 'r') as f_inp:
        data = json.load(f_inp)
    rows = []
    for level, users in data.items():
        for id, name in users.items():
            rows.append({'level': level,
                         'name': name,
                         'id': id})
    with open(f'{filename}.csv', 'w', newline='') as res:
        csv_write = csv.DictWriter(res, fieldnames=['level',
                                                    'name',
                                                    'id'])
        csv_write.writeheader()
        csv_write.writerows(rows)


def read_csv(filename: str):
    with open(f'{filename}.csv', 'r', encoding='UTF-8') as inp:
        data = inp.read().split('\n')
    res = []
    for value in data[:-1]:
        print(value)
        level, name, id = value[:].split(',')
        res.append({'id': f'{id:06}', 'level': level, 'name': name, 'hash': hash(id + name)})

    with open(f'{filename}new.json', 'w', encoding='UTF-8') as out:
        json.dump(res, out, indent=4)


if __name__ == '__main__':
    # json_to_csv('users')
    read_csv('users')
