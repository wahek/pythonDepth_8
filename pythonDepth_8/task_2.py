import json

# {
#     level: {
#         id: name,
#         ...
#     }
#     ...
# }

import json


def uniq_id(data: dict, id: str) -> bool:
    for item in data.values():
        if id in item.keys():
            return False
        return True


def enter_id_name(name_file: str) -> None:
    name_file += ".json"

    while True:
        id_ = input("id: ")
        name = input("name: ")
        level = input("level: ")

        try:
            with open(name_file, 'r', encoding='utf-8') as fr:
                read_dict: dict = json.load(fr)

        except FileNotFoundError:
            read_dict: dict = {str(i): {} for i in range(1, 8, 1)}

        read_dict[level].update({id_: name})

        with open(name_file, 'w', encoding='utf-8') as fw:
            json.dump(read_dict, fw, indent=2)


if __name__ == "__main__":
    enter_id_name(name_file='users')
