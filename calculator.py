"""Модуль с арифметическими операциями."""


def subtract(a, b):
    """Вернуть разность a и b."""
    return a - b


def multiply(a, b):
    """Вернуть произведение a и b."""
    return a * b


def divide(a, b):
    """Вернуть частное a и b; при делении на ноль — ZeroDivisionError."""
    if b == 0:
        raise ZeroDivisionError("Деление на ноль")
    return a / b


def power(a, b):
    """Вернуть a в степени b."""
    return a ** b
