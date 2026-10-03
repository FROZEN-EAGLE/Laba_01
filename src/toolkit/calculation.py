import operator

from .errors import DivisionByZeroError
from .validation import Num, Unary, Binary, Expression


operations = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "//": operator.floordiv,
    "%": operator.mod,
}

unary_oper = {
    "+": operator.pos,
    "-": operator.neg,
}


def calc(node: Expression) -> float:
    if isinstance(node, Num):
        return node.value

    if isinstance(node, Unary):
        operation = unary_oper[node.operator]
        return operation(calc(node.operand))

    if isinstance(node, Binary):
        left = calc(node.left)
        right = calc(node.right)

        operation = operations[node.operator]

        try:
            return operation(left, right)
        except ZeroDivisionError as error:
            raise DivisionByZeroError() from error

    raise TypeError()