"""Модуль с дополнительным функционалом."""


from typing import List, Dict, Optional
from .validators import EmailValidater, DateValidater, PhoneValidater
from pymongo.collection import Collection
from collections import Counter
from copy import deepcopy


def match_checking(
    check_dict: dict, db_collection: Collection
) -> Optional[str]:
    """Проверка совпадений типов параметров запроса и документов в бд."""

    # список имен шаблонов со совпадающими полями
    document_list: List[str] = []

    for key, value in check_dict.items():
        if DateValidater.is_valid(value):
            document = db_collection.find_one({key: value})
            if document:
                document_list.append(document['name'])

        if len(value) == 16:
            value_ = '+' + value[1:]
            if PhoneValidater.is_valid(value_):
                document = db_collection.find_one({key: value})
                if document:
                    document_list.append(document['name'])

        if EmailValidater.is_valid(value):
            document = db_collection.find_one({key: value})
            if document:
                document_list.append(document['name'])

    # проверить список найденных совпадений
    if document_list:

        # самый подходящий документ
        name_document = max(Counter(document_list))

        response = field_reconciliation(
            check_dict, name_document, db_collection
        )
        return response
    return False


def field_reconciliation(
    check_dict: dict, name_document: str, db_collection: Collection
):
    """Проверка наличий всех полей шаблона в параметрах запроса."""
    document: dict = db_collection.find_one({'name': name_document})
    copy_document = deepcopy(document)

    # удалить не нужные поля перед проверкой вхождения ключей
    copy_document.pop('name', False)
    copy_document.pop('_id', False)

    for key, value in copy_document.items():
        if (key in check_dict and check_dict[key] == value) or (
            key in check_dict and '+' + check_dict[key][1:] == value
        ):
            continue
        else:
            return False

    return name_document


def define_field_type(check_dict: dict) -> dict:
    """Определение типа полей для параметров с ненайденным шаблоном."""

    for key, value in check_dict.items():
        if DateValidater.is_valid(value):
            check_dict[key] = 'DateType'
            continue

        if len(value) == 16:
            value_ = '+' + value[1:]
            if PhoneValidater.is_valid(value_):
                check_dict[key] = 'PhoneType'
                continue

        if EmailValidater.is_valid(value):
            check_dict[key] = 'EmailType'
            continue

        else:
            check_dict[key] = 'TextType'

    return check_dict
