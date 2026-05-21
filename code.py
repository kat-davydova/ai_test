from cli import main


if __name__ == '__main__':
    raise SystemExit(main())
def is_leap(year: int) -> bool:
    """Возвращает True, если год високосный.

    Параметры:
        year: положительный целый год.

    Исключения:
        TypeError: если год не является целым числом.
        ValueError: если год не положительный.
    """
    # Проверка типа: bool наследуется от int, но не считается корректным годом.
    if isinstance(year, bool) or not isinstance(year, int):
        raise TypeError('Год должен быть целым числом.')
    # Год должен быть положительным, ноль и отрицательные значения недопустимы.
    if year <= 0:
        raise ValueError('Год должен быть положительным целым числом.')
    # Год високосный, если он делится на 4, но не на 100, кроме случаев, когда он делится на 400.
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


if __name__ == '__main__':
    import argparse
    import sys

    import re

    parser = argparse.ArgumentParser(description='Проверка, является ли год високосным')
    parser.add_argument('year', nargs='*', help='Год для проверки (если не задан — показываются примеры)')
    args = parser.parse_args()

    def _human(b: bool) -> str:
        return 'Високосный' if b else 'Невисокосный'

    MAX_DIGITS = 6

    if len(args.year) == 0:
        examples = [1900, 2000, 2024, 2023]
        for y in examples:
            print(f"{y}: {_human(is_leap(y))}")
        sys.exit(0)

    if len(args.year) > 1:
        print(
            f"Ошибка: ожидается один аргумент года, а получено {len(args.year)}."
            f" Если нужно ввести специальный символ, оберните его в кавычки: python3 code.py '!'",
            file=sys.stderr,
        )
        sys.exit(2)

    raw = args.year[0]
    if not re.fullmatch(r'[+-]?\d+', raw):
        print(f"Ошибка: '{raw}' — ожидается целое число.", file=sys.stderr)
        sys.exit(2)
    digits = raw.lstrip('+-').lstrip('0') or '0'
    if len(digits) > MAX_DIGITS:
        print(f"Ошибка: слишком длинное число ({len(digits)} цифр). Максимум {MAX_DIGITS} цифр.", file=sys.stderr)
        sys.exit(2)
    year = int(raw)
    if year <= 0:
        print(f"Ошибка: {year} — некорректный год. Год должен быть положительным целым числом.", file=sys.stderr)
        sys.exit(2)
    print(_human(is_leap(year)))
