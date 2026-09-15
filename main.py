"""Точка входа проекта: калькулятор для лабораторной работы № 1."""

from calculator import divide, multiply, power, subtract

__version__ = "1.0.1"


def add(a, b):
    """Вернуть сумму двух чисел."""
    return a + b


def main():
    """Вывести приветствие и примеры вычислений."""
    print(f"Калькулятор v{__version__}")
    print("2 + 3 =", add(2, 3))
    print("5 - 3 =", subtract(5, 3))
    print("4 * 6 =", multiply(4, 6))
    print("9 / 3 =", divide(9, 3))
    print("2 ** 8 =", power(2, 8))


if __name__ == "__main__":
    main()
