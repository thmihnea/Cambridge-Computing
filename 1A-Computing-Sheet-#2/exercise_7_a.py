import numpy as np

MAX_STACK: int = 100
TOLERANCE: float = 1e-8

if __name__ == "__main__":

    def f(x: float):
        return x ** 3 + x ** 2
    
    def df(x: float):
        return 3 * x ** 2 + 2 * x
    
    def ddf(x: float):
        return 6 * x + 2

    guess: float = 0.5
    initial: float = np.abs(df(guess))

    for _ in range(MAX_STACK):
        x: float = guess - df(guess) / ddf(guess)
        guess = x

        current: float = np.abs(df(x))
        if current / initial < TOLERANCE:
            break

    print(f"""
          The value which optimizes the function within the allowed tolerance is {guess}.
          The value we obtain for this value of x is {f(guess)}.
          """)