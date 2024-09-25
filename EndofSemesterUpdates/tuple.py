def add(a: int, b: int) -> int:
    """Returns the sum of two integers."""
    return a + b

def divide_and_remainder(a: int, b: int) -> tuple[int, int]:
    """Returns the quotient and remainder of the division of two integers."""
    return (a // b, a % b)

def generate_series(start: float, stop: float, step: float) -> list[float]:
    """Returns a list of floating-point numbers in the range [start, stop) with the given step."""
    return [x for x in range(int(start), int(stop), int(step))]