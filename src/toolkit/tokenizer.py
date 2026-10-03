from dataclasses import dataclass
from enum import Enum
from .errors import (
    EmptyExpressionError,
    InvalidCharacterError,
    InvalidNumberError,
)


class TokenType(Enum):
    num = "NUMBER"
    operator = "OPERATOR"


@dataclass
class Token:
    type: TokenType
    value: float | str
    position: int


def tokenize(exp: str):
    if not exp.strip():
        raise EmptyExpressionError()

    tokens: list[Token] = []
    position = 0

    while position < len(exp):
        char = exp[position]

        if char.isspace():
            position += 1
            continue

        if char in "+-*/":
            tokens.append(
                Token(
                    type=TokenType.operator,
                    value=char,
                    position=position,
                )
            )
            position += 1
            continue

        if char.isdigit() or char == ".":
            start = position
            dot_count = 0

            while position < len(exp):
                char = exp[position]

                if char.isdigit():
                    position += 1
                    continue

                if char == ".":
                    dot_count += 1
                    position += 1

                    if dot_count > 1:
                        raise InvalidNumberError()

                    continue

                break

            num_text = exp[start:position]

            if num_text == ".":
                raise InvalidNumberError()

            tokens.append(
                Token(
                    type=TokenType.num,
                    value=float(num_text),
                    position=start,
                )
            )
            continue

        raise InvalidCharacterError()

    return tokens