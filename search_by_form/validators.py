"""Модуль с валидаторами полей."""

import re


class EmailValidater:
    """Класс проверки поля почты."""

    regex = re.compile(
        r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
    )

    @classmethod
    def is_valid(cls, email: str) -> bool:
        """Проверка поля почты."""

        if re.fullmatch(cls.regex, email):
            return True
        return False


class DateValidater:
    """Класс проверки поля даты."""

    # DD.MM.YYYY YYYY-MM-DD

    regex1 = re.compile(r'\d\d.\d\d.\d{4}')
    regex2 = re.compile(
        r'(19\d\d|20\d\d)[-/](0[1-9]|1[0-2])[-/](0[1-9]|[12]\d|3[01])'
    )

    @classmethod
    def is_valid(cls, format_date: str) -> bool:
        """Проверка поля даты."""
        if re.fullmatch(cls.regex1, format_date) or re.fullmatch(
            cls.regex2, format_date
        ):
            return True
        return False


class PhoneValidater:
    """Класс проверки поля телефонного номера."""

    regex = re.compile(r'\+7\s\d{3}\s\d{3}\s\d{2}\s\d{2}')

    @classmethod
    def is_valid(cls, format_date: str) -> bool:
        """Проверка телефонного номера."""
        if re.fullmatch(cls.regex, format_date):
            return True
        return False
