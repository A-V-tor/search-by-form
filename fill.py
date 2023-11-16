"""Модуль наполнения бд документами."""


from search_by_form.db import collection
import json


def make_fill():
    with open('datalist.json', 'r') as f:
        collection.insert_many(json.load(f))


if __name__ == '__main__':
    make_fill()
