class Calculator:
    def __init__(self, value=0):
        self.value = value

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return Calculator(self.value + other)
        elif isinstance(other, Calculator):
            return Calculator(self.value + other.value)
        else:
            raise TypeError("Операция сложения возможна только с числами или экземплярами класса Calculator")

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            return Calculator(self.value - other)
        elif isinstance(other, Calculator):
            return Calculator(self.value - other.value)
        else:
            raise TypeError("Операция вычитания возможна только с числами или экземплярами класса Calculator")

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Calculator(self.value * other)
        elif isinstance(other, Calculator):
            return Calculator(self.value * other.value)
        else:
            raise TypeError("Операция умножения возможна только с числами или экземплярами класса Calculator")

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            if other == 0:
                raise ValueError("Деление на ноль невозможно")
            return Calculator(self.value / other)
        elif isinstance(other, Calculator):
            if other.value == 0:
                raise ValueError("Деление на ноль невозможно")
            return Calculator(self.value / other.value)
        else:
            raise TypeError("Операция деления возможна только с числами или экземплярами класса Calculator")

    def __str__(self):
        return str(self.value)


if __name__ == "__main__":
    calc1 = Calculator(10)
    calc2 = Calculator(5)

    print(calc1 + calc2)
    print(calc1 - calc2)
    print(calc1 * calc2)
    print(calc1 / calc2)
