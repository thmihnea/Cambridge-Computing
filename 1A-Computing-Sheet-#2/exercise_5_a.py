import numpy as np
import matplotlib.pyplot as plt
from typing import List, Callable

INTERVAL_MIN: float = 0
INTERVAL_MAX: float = 2 * np.pi
AMOUNT: int = 50

def average(arr: List[float]) -> List[float]:
    length = len(arr)
    values: List[float] = [0] * length

    for i in range(1, length - 1):
        values[i] = (arr[i - 1] + arr[i] + arr[i + 1]) / 3.0

    values[0] = arr[0]
    values[-1] = arr[-1]
    
    return values

if __name__ == "__main__":
    x: List[float] = np.linspace(INTERVAL_MIN, INTERVAL_MAX, AMOUNT)
    f: List[float] = np.sin(x) + np.cos(10 * x) / 5
    avg: List[float] = average(f)

    plt.plot(x, f)
    plt.plot(x, avg)
    plt.show()

    