"""Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории. Результаты
обхода сохраните в файлы json, csv и pickle.
Для дочерних объектов указывайте родительскую директорию.
Для каждого объекта укажите файл это или директория.
Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и
директорий."""
import csv
import json
import os
import pickle


def path_to_dict(direction: str = '.'):
    dict_of_dir = list()
    for path, directs, files in os.walk(direction):
        *_, current_dir = path.split('\\')
        try:
            *_, parent_dir, _ = path.split('\\')
        except ValueError:
            parent_dir = 'relative path'
        size_of_dir = 0
        size = 0
        for file in files:
            current_path = path + file
            fp = os.path.join(path, file)
            print(fp)
            size += os.path.getsize(fp)
            dict_of_dir.append({'name': file, 'parent': current_dir, 'type': 'file',
                                'size': file.__sizeof__()})
        dict_of_dir.append({'name': current_dir, 'parent': parent_dir, 'type': 'dir',
                            'size': size})
    return dict_of_dir


def dict_to_json(dictionary: dict, filename: str):
    with open(f'{filename}.json', 'w', encoding='UTF-8') as out:
        json.dump(dictionary, out, indent=4)


def dict_to_csv(dictionary: dict, filename: str):
    with open(f'{filename}.csv', 'w', encoding='UTF-8', newline='') as out:
        print(dictionary[0])
        csv_write = csv.DictWriter(out, fieldnames=['name', 'parent', 'type', 'size'])
        csv_write.writeheader()
        csv_write.writerows(dictionary)


def dict_to_pickle(dictionary: dict, filename: str):
    with open(f'{filename}.pickle', 'wb') as out:
        pickle.dump(dictionary, out)


res_dict = path_to_dict()
dict_to_json(res_dict, 'path_to_JSON')
dict_to_csv(res_dict, 'path_to_CSV')
dict_to_pickle(res_dict, 'path_to_PIKLE')
