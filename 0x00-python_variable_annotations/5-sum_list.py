#!/usr/bin/env python3
"""scripting"""


def sum_list(input_list: list[float]) -> float:
    """Calculates the sum of all elements in a list of floats.
    Args:
    input_list: A list containing float values.
    Returns:
    The sum of all elements in the list as a float.
    """
    # Leverage the built-in sum function with type hinting
    return sum(input_list)
