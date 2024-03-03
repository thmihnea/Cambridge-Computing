import cmath # Use this for handling complex numbers.
from typing import Callable, List, Dict

def complex_step(func: Callable, x: float, h: float) -> float:
    result: complex = func(x + h * 1j)
    return result.imag / h

def two_sided(func: Callable, x: float, h: float) -> float:
    return (func(x + h) - func(x - h)) / (2 * h)

if __name__ == "__main__":
    # Define the function we require.
    def func(x: float) -> float:
        return x ** 2 * cmath.sin(x ** 2)
    
    # Actual derivative.
    def derivative(x: float) -> float:
        return 2 * x * (cmath.sin(x ** 2) + x ** 2 * cmath.cos(x ** 2))
    
    # Setup required DS's.
    errors: List[float] = [10 ** -9, 10 ** -12, 10 ** -15]
    values: List[int] = [10, 100, 1000, 10000]

    complex_results: Dict[float, float] = dict()
    two_sided_results: Dict[float, float] = dict()

    # Helper function for clean code.
    def append(key: float, value: float, table: Dict):
        if key not in table:
            table[key] = [value]
        else:
            table[key].append(value)

    # Gather data.
    for x in values:
        for error in errors:
            complex_val: float = complex_step(func, x, error)
            two_sided_val: float = two_sided(func, x, error)
            append(x, complex_val, complex_results)
            append(x, two_sided_val, two_sided_results)

    # Display data.
    for x in values:
        actual: float = derivative(x)
        print(f"Showing results for x = {x}.")
        for i in range(len(errors)):
            print(f"""Approximating the derivative for h={errors[i]}.
                  Complex step: {abs(complex_results[x][i] - actual)}.
                  Two-sided step: {abs(two_sided_results[x][i] - actual)}.""")


    
    