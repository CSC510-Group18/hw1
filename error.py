#!/usr/bin/env python3


class Parent:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f"Parent: {self.name}"


class Child(Parent):
    def __init__(self, name: str):
        super().__init__(name)

    def __str__(self):
        return f"Child: {self.name}"


def square(x: int | float) -> int | float:
    """Square a number

    Args:
        x: The number to square

    Returns:
        The square of the number
    """
    return x * x


if __name__ == "__main__":
    a = 0
    b = 1

    for i in range(1000):
        tmp = a + b
        a = b
        b = tmp

    print(a)
