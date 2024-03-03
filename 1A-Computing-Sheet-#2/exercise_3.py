from typing import List, Callable
import math

ENTRIES_LIMIT: int = 5

def first_order(func: Callable, x: float, h: float) -> float:
    return (func(x + h) - func(x))/h

def second_order(func: Callable, x: float, h: float) -> float:
    return (func(x + h) - func(x - h))/(2*h)

if __name__ == "__main__":
    # Construct error list.
    errors: List[float] = [10 ** -i for i in range(ENTRIES_LIMIT + 1)]

    # We will use the sine function because Python has already
    # implementede its derivative so we can easily look up the error.
    func: Callable = math.sin
    x: float = 5
    derivative: Callable = math.cos

    # Setup required data structures to store approximations.
    first_order_approx: List[float] = []
    second_order_approx: List[float] = []

    # Compute approximations.
    for entry in errors:
        first_order_approx.append(
            first_order(func, x, entry)
        )
        second_order_approx.append(
            second_order(func, x, entry)
        )

    # Compute errors.
    for i in range(ENTRIES_LIMIT):
        error_fo: float = abs(
            first_order_approx[i] - derivative(x)
        )
        error_so: float = abs(
            second_order_approx[i] - derivative(x)
        )

        print(f"""Computing error with h = 10^-{i}.
              First order approximation error: {error_fo}.
              Second order approximation error: {error_so}.""")