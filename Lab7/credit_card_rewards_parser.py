
import re


def mask_card_number(number):
    """
    Hide all but the last four digits of a card number.

    Accepts a string containing digits, spaces and hyphens.
    Returns None if the input is invalid.
    """
    if not isinstance(number, str):
        return None

    digits = number.replace(" ", "").replace("-", "")

    if not digits or not digits.isascii() or not digits.isdigit():
        return None

    if len(digits) < 4:
        return None

    return "*" * (len(digits) - 4) + digits[-4:]


def parse_transaction(line):
    """
    Parse 'date,category,amount' into a (category, amount) tuple.

    Returns None if the input is invalid.
    """
    if not isinstance(line, str):
        return None

    parts = line.split(",")

    if len(parts) != 3:
        return None

    date, category, amount = parts

    date = date.strip()
    category = category.strip()
    amount = amount.strip()

    if not date or not category:
        return None

    if not re.fullmatch(r"[+-]?[0-9]+", amount):
        return None

    try:
        amount_value = int(amount)
    except (ValueError, OverflowError):
        return None

    return category.lower(), amount_value


def parse_statement_total(text):
    """
    Extract a whole-number amount from a line such as 'Total: 12,500'.

    Accepts correctly grouped commas.
    Returns None if the input is invalid.
    """
    if not isinstance(text, str):
        return None

    prefix, separator, amount = text.partition(":")

    if not separator:
        return None

    amount = amount.strip()

    # Accept numbers such as 12500, 12,500 and -12,500.
    valid_amount = re.fullmatch(
        r"[+-]?(?:[0-9]+|[0-9]{1,3}(?:,[0-9]{3})+)",
        amount
    )

    if not valid_amount:
        return None

    try:
        return int(amount.replace(",", ""))
    except (ValueError, OverflowError):
        return None


def main():
    print("==== Running mask_card_number ====")
    value = input(
        "Enter a card number (e.g. 4111 1111 1111 1234): "
    )
    print("Masked card number:", mask_card_number(value))

    print("\n==== Running parse_transaction ====")
    value = input(
        "Enter a transaction as DATE,CATEGORY,AMOUNT "
        "(e.g. 2026-11-05,dining,1550): "
    )
    print("Category and amount:", parse_transaction(value))

    print("\n==== Running parse_statement_total ====")
    value = input(
        "Enter the statement total line (e.g. Total: 12,500): "
    )
    print("Statement total:", parse_statement_total(value))


if __name__ == "__main__":
    main()
