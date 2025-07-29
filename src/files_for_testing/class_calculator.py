class Calculator:
    def divide(self, x: int | float, y: int | float) -> int | float:
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Both arguments should be numeric")
        if y == 0:
            raise ZeroDivisionError("Cannot divide be zero")
        return x / y

    def add(self, x: int | float, y: int | float) -> int | float:
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Both arguments should be numeric")
        return x + y


if __name__ == "__main__":
    calculator = Calculator()
