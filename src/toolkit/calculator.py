from .tokenizer import tokenize
from .validation import parse_exp
from .calculation import calc


def calculate(exp: str) -> float:
    tokens = tokenize(exp)
    tree = parse_exp(tokens)
    return calc(tree)