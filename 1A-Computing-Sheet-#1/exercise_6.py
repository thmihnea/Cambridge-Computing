import math

def estimate(f, a, b, x, w):
    n = len(w)
    sum = 0
    for i in range(0, n):
        sum += w[i] * f(x[i])
    return (b - a) * sum

def function(x):
    return x ** 3 + x ** 2

def error(x, y):
    return abs(x - y)

def main():
    a = 0; b = 10
    actual = 8500 / 3

    trapezoidal_weights = [1/2, 1/2]; trapezoidal_points = [a, b]
    simpson_weigths = [1/6, 2/3, 1/6]; simpson_points = [a, (a + b) / 2, b]
    gauss_weigths = [1/2, 1/2]; gauss_points = [(1/2) * (a + b - (b - a) / math.sqrt(3)), 
                                                (1/2) * (a + b + (b - a) / math.sqrt(3))]
    
    trapezoidal = estimate(function, a, b, trapezoidal_points, trapezoidal_weights)
    simpson = estimate(function, a, b, simpson_points, simpson_weigths)
    gauss = estimate(function, a, b, gauss_points, gauss_weigths)

    print(f'Integral estimated at {trapezoidal} for Trapezoidal, {simpson} for Simpson\'s and {gauss} for Gauss.')
    print(f'Errors are {error(trapezoidal, actual)}, {error(simpson, actual)}, and {error(gauss, actual)} respectively.')

if __name__ == '__main__':
    main()
