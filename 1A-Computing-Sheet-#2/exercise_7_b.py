import numpy as np
from typing import Callable, List

MAXIMUM_STACK: int = 10000
TOLERANCE: float = 1e-9

CONST_A: float = 2
CONST_B: float = 100

class Function:

    def __init__(self, f: Callable, fx: Callable, fy: Callable, fxx: Callable, fxy: Callable, fyy: Callable):
        self.f = f
        self.fx = fx
        self.fy = fy
        self.fxx = fxx
        self.fxy = fxy
        self.fyy = fyy

def hessian(vec: List[float], function: Function) -> List[List[float]]:
    fxx: Callable = function.fxx
    fxy: Callable = function.fxy
    fyy: Callable = function.fyy

    return np.array([
        [fxx(vec), fxy(vec)],
        [fxy(vec), fyy(vec)]
    ])

def g(vec: List[float], function: Function) -> List[float]:
    fx: Callable = function.fx
    fy: Callable = function.fy

    return np.array([fx(vec), fy(vec)])

def newton(guess: List[float], function: Function) -> List[float]:
    initial_norm: float = np.linalg.norm(guess)
    for _ in range(MAXIMUM_STACK):
        x: List[float] = guess - np.linalg.solve(hessian(guess, function), g(guess, function))
        guess = x

        current_norm: float = np.linalg.norm(x)
        if current_norm / initial_norm < TOLERANCE:
            return x
    return guess


if __name__ == "__main__":
    def f(vec: List[float]) -> float:
        x: float = vec[0]
        y: float = vec[1]

        return (CONST_A - x) ** 2 + CONST_B * (y - x ** 2) ** 2
    
    def fx(vec: List[float]) -> float:
        x: float = vec[0]
        y: float = vec[1]

        return -2 * (CONST_A - x) - 4 * CONST_B * x * (y - x ** 2)

    def fy(vec: List[float]) -> float:
        x: float = vec[0]
        y: float = vec[1]

        return 2 * CONST_B * (y - x ** 2)

    def fxx(vec: List[float]) -> float:
        x: float = vec[0]
        y: float = vec[1]

        return 2 + 12 * CONST_B * x ** 2 - 4 * CONST_B * (y - x ** 2)

    def fxy(vec: List[float]) -> float:
        x: float = vec[0]

        return -4 * CONST_B * x

    def fyy(vec: List[float]) -> float:
        return 2 * CONST_B

    function: Function = Function(
        f,
        fx,
        fy,
        fxx,
        fxy,
        fyy
    )

    guess: List[float] = np.array([1.1, 1.1])
    result: List[float] = newton(guess, function)
    gradient: List[float] = g(result, function)

    print(f"""
          The solution we obtain is the vector x = [{result[0]}, {result[1]}].
          The value of the function at this point is f(x) = {f(result)}.
          The value of its gradient is grad f = [{gradient[0]}, {gradient[1]}].
          """)