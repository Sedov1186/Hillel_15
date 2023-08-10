class NegativeDegree(Exception):
    def __init__(self, message='Возведение в отрицательную степень'):
        self.message = message
        super().__init__(self.message)


class Calculator:
    def __init__(self, var):
        self.var = var

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return Calculator(self.var + other)
        raise TypeError('Нельзя складывать цифры и буквы!')

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            return Calculator(self.var - other)
        raise TypeError('Нельзя от цифры отнять буквы!')

    def __pow__(self, power, modulo=None):
        if power >= 0:
            return Calculator(self.var ** power)
        raise NegativeDegree()

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError('Нельзя делить на ноль!')
            return Calculator(self.var / other)
        raise TypeError('Нельзя делить на буквы!')

try:
    calc = Calculator(5)
    result = calc ** 2
    print(result.var)

    result = calc / 2
    print(result.var)

    result = calc + 10
    print(result.var)

    result = calc - 3
    print(result.var)

    result = calc + 'test'
    print(result.var)
except Exception as ex:
    print(f'Error: {ex}')