from .errors import (AbsoluteZeroError, InvalidNumberError, UnknownUnitError)


len_to_m = {
    "mm": 0.001,
    "cm": 0.01,
    "m": 1.0,
    "km": 1000.0,
}

mass_to_kg = {
    "g": 0.001,
    "kg": 1.0,
}

temp_un = {"c", "f", "k"}


def norm_unit(unit: str) -> str:
    return unit.strip().lower()


def get_group(unit: str) -> str:
    normal = norm_unit(unit)

    if normal in len_to_m:
        return "length"

    if normal in mass_to_kg:
        return "mass"

    if normal in temp_un:
        return "temperature"

    raise UnknownUnitError()


def parse_value(value: str | float | int):
    try:
        return float(value)
    except (TypeError, ValueError) as error:
        raise InvalidNumberError() from error


def valid_temp(value: float, unit: str):
    if unit == "c" and value < -273.15:
        raise AbsoluteZeroError()

    if unit == "f" and value < -459.67:
        raise AbsoluteZeroError()

    if unit == "k" and value < 0:
        raise AbsoluteZeroError()


def temp_to_cel(value: float, unit: str):
    if unit == "c":
        return value

    if unit == "f":
        return (value - 32.0) * 5.0 / 9.0

    return value - 273.15


def cel_to_temp(value: float, unit: str):
    if unit == "c":
        return value

    if unit == "f":
        return value * 9.0 / 5.0 + 32.0

    return value + 273.15


def convert(
    value: str | float | int,
    from_unit: str,
    to_unit: str,):
    value_float = parse_value(value)

    source = norm_unit(from_unit)
    target = norm_unit(to_unit)

    sour_group = get_group(source)
    targ_group = get_group(target)

    if sour_group != targ_group:
        raise IncompatibleUnitsError()

    if sour_group == "length":
        base_value = value_float * len_to_m[source]
        return float(base_value / len_to_m[target])

    if sour_group == "mass":
        base_value = value_float * mass_to_kg[source]
        return float(base_value / mass_to_kg[target])

    valid_temp(value_float, source)

    celsius = temp_to_cel(value_float, source)
    result = cel_to_temp(celsius, target)

    return float(result)