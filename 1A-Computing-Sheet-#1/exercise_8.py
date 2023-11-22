import math
import random

def random_distribution(a, b, length):
    distribution = []
    for i in range(0, length):
        distribution.append(random.uniform(a, b))
    return distribution

def monte_carlo(f, a, b, N):
    x = random_distribution(-abs(a), abs(a), N)
    y = random_distribution(-abs(b), abs(b), N)
    integral = 0
    for i in range(0, N):
        integral += f(x[i], y[i])
    return 4 * abs(a*b) / N * integral

def f(x, y):
    return math.exp(x * y) * (math.cos(y) ** 2) * (math.sin(x) ** 2)

def circle(x, y):
    return 1 if x ** 2 + y ** 2 < 1 else 0

def main():
    N = [10 ** 2, 10 ** 5, 10 ** 6]
    for sample_size in N:
        estimation = monte_carlo(
            f,
            -1,
            1,
            sample_size
        )
        print(f'Estimation for (a) using N = {sample_size} points: {estimation}')
    print(f'Estimation of pi: {monte_carlo(circle, -1, 1, 10 ** 6)}')
    

if __name__ == '__main__':
    main()
