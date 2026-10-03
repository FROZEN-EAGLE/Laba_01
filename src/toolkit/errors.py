class CalculatorError(Exception):
    pass
    # Потенциальные ошибки

class EmptyExpressionError(CalculatorError):
    pass
    # Пустое выражение

class InvalidCharacterError(CalculatorError):
    pass
    # Недопустимый символ

class InvalidNumberError(CalculatorError):
    pass
    # Неправильный формат

class InvalidExpressionError(CalculatorError):
    pass
    # Невозможная структура

class MissingOperandError(CalculatorError):
    pass
    # Отсутсвует операнд

class DivisionByZeroError(CalculatorError):
    pass
    # Попытка поделить на ноль
class AbsoluteZeroError(CalculatorError):
    pass
    # Температура ниже абсолютного нуля
class UnknownUnitError(CalculatorError):
    pass
    # Неизвестная переменная
class IncompatibleUnitsError(CalculatorError):
    pass
    # Несовместимые единицы