import json


def serial():
    with open('text.txt', 'r', encoding='UTF-8') as data:
        res = data.read().split('\n')[:-1]
    res = [{i.split()[0].capitalize(): i.split()[1]}for i in res]
    print(res)
    with open('rext_json.txt', 'w') as data_out:
        json.dump(res, data_out, indent=2)


serial()
