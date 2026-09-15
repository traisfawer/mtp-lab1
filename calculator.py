"""Модуль с арифметическими операциями."""


def subtract(a, b):
    """Вернуть разность a и b."""
    return a - b


def multiply(a, b):
    """Вернуть произведение a и b."""
    return a * b


def divide(a, b):
    """Вернуть частное a и b; при делении на ноль — ValueError."""
    if b == 0:
        raise ValueError("Деление на ноль")
    return a / b
