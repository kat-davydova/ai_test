"""Модуль высокосного года."""


def is_leap(year: int) -> bool:
    """Возвращает True, если год високосный."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def format_result(is_leap_year: bool) -> str:
    """Возвращает человекопонятный результат для вывода."""
    return "Високосный" if is_leap_year else "Невисокосный"
