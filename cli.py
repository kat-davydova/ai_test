"""CLI для проверки високосного года."""

from __future__ import annotations

import argparse
import re
import sys
from typing import Iterable

from leap import format_result, is_leap

MAX_DIGITS = 6
YEAR_PATTERN = re.compile(r"[+-]?\d+")


def parse_args(argv: Iterable[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Проверка, является ли год високосным",
    )
    parser.add_argument(
        "year",
        nargs="*",
        help="Год для проверки (если не задан — показываются примеры)",
    )
    return parser.parse_args(argv)


def validate_year_string(raw: str) -> int:
    if not YEAR_PATTERN.fullmatch(raw):
        raise ValueError(f"Ошибка: '{raw}' — ожидается целое число.")

    digits = raw.lstrip('+-').lstrip('0') or '0'
    if len(digits) > MAX_DIGITS:
        raise ValueError(
            f"Ошибка: слишком длинное число ({len(digits)} цифр). Максимум {MAX_DIGITS} цифр."
        )

    year = int(raw)
    if year <= 0:
        raise ValueError(
            f"Ошибка: {year} — некорректный год. Год должен быть положительным целым числом."
        )

    return year


def print_examples() -> None:
    examples = [1900, 2000, 2024, 2023]
    for year in examples:
        print(f"{year}: {format_result(is_leap(year))}")


def main(argv: Iterable[str] | None = None) -> int:
    args = parse_args(argv)

    if len(args.year) == 0:
        print_examples()
        return 0

    if len(args.year) > 1:
        print(
            (
                f"Ошибка: ожидается один аргумент года, а получено {len(args.year)}."
                f" Если нужно ввести специальный символ, оберните его в кавычки: python3 code.py '!'"
            ),
            file=sys.stderr,
        )
        return 2

    try:
        year = validate_year_string(args.year[0])
    except ValueError as error:
        print(error, file=sys.stderr)
        return 2

    print(format_result(is_leap(year)))
    return 0
