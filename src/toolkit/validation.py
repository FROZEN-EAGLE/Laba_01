from dataclasses import dataclass

from .errors import InvalidExpressionError, MissingOperandError
from .tokenizer import Token, TokenType


@dataclass
class Num:
    value: float


@dataclass
class Unary:
    operator: str
    operand: Num


@dataclass
class Binary:
    left: "Expression"
    operator: str
    right: "Expression"


Expression = Num | Unary | Binary


class parser:
    def __init__(self, tokens: list[Token]):
        self.tokens = tokens
        self.position = 0

    def parse(self):
        result = self.parse_expression()

        if self.position != len(self.tokens):
            raise InvalidExpressionError()

        return result

    def parse_expression(self):
        result = self.parse_term()

        while self.operator1({"+", "-"}):
            operator = self.cons().value
            result = Binary(result, operator, self.parse_term())

        return result

    def parse_term(self):
        result = self.parse_unary()

        while self.operator1({"*", "/", "//", "%"}):
            operator = self.cons().value
            result = Binary(result, operator, self.parse_unary())

        return result

    def parse_unary(self):
        if self.operator1({"+", "-"}):
            operator = self.cons().value

            if self.position >= len(self.tokens):
                raise MissingOperandError()

            if self.tokens[self.position].type != TokenType.num:
                raise MissingOperandError()

            return Unary(operator, Num(self.cons().value))

        return self.parse_num()

    def parse_num(self):
        if self.position >= len(self.tokens):
            raise MissingOperandError()

        token = self.tokens[self.position]

        if token.type != TokenType.num:
            raise MissingOperandError()

        self.position += 1
        return Num(token.value)

    def operator1(self, operator):
        if self.position >= len(self.tokens):
            return False

        token = self.tokens[self.position]
        return token.type == TokenType.operator and token.value in operator

    def cons(self):
        token = self.tokens[self.position]
        self.position += 1
        return token


def parse_exp(tokens: list[Token]):
    return parser(tokens).parse()



