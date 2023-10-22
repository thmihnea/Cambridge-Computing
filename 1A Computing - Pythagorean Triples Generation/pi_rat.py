import math

# O(n^3) complexity of the pi_rat algorithm.
def pi_rat(limit):
    minimum_distance = 1e9
    sides = ()
    for i in range(1, limit):
        for j in range(i, limit):
            for k in range(j, limit):
                if k * k != i * i + j * j: continue
                distance = compute_distance(i, j, k)
                if distance < minimum_distance: 
                    minimum_distance = distance
                    sides = (i, j, k)
    return sides

# Optimized version of pi_rat_o.
# Complexity is O(n^2), generating pairs using (x, y, z) = (m^2 - n^2, 2mn, m^2 + n^2).
def pi_rat_o(limit):
    minimum_distance = 1e9
    root = math.isqrt(limit)
    sides = ()
    for m in range(1, root):
        for n in range(1, root):
            if m == n or m ** 2 - n ** 2 < 0 or m ** 2 + n ** 2 > limit: continue
            x = min(m * m - n * n, 2 * m * n)
            y = max(m * m - n * n, 2 * m * n)
            z = m * m + n * n
            distance = compute_distance(x, y, z)
            if distance < minimum_distance:
                minimum_distance = distance
                sides = (x, y, z)
    return sides

def compute_distance(i, j, k):
    return abs(j/i - math.pi)

def main():
    print(pi_rat_o(50))

if __name__ == "__main__":
    main()