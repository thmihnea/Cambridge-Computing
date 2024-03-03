import math
from typing import List

def linear_search_time(n: int) -> float:
    return 10 ** (-8) * n

def binary_search_time(n: int) -> float:
    return 10 ** (-6) * math.log(n)

def sort_time(n: int) -> float:
    return 2 * 10 ** (-5) * n * math.log(n)

if __name__ == "__main__":
    n: int = 26 * 10 ** 6
    values: List[int] = [10 ** 3, 10 ** 4, 3 * 10 ** 5, 5 * 10 ** 5]

    def linear_search(n: int, m: int) -> float:
        return m * linear_search_time(n)
    
    def sort_binary_search(n: int, m: int) -> float:
        return sort_time(n) + m * binary_search_time(n)
    
    # Part (a)

    for entry in values:
        print(f"""Performing calculations for m = {entry}. 
              Time for linear search is {linear_search(n, entry)}. 
              Time for sorting and binary search is {sort_binary_search(n, entry)}.""")
        
    # Part (b)
        
    m: int = 0
    time_linear_search: float = float("-inf")
    time_binary_search: float = float("inf")

    while time_linear_search < time_binary_search:
        time_linear_search = linear_search(n, m)
        time_binary_search = sort_binary_search(n, m)
        m += 1

    print(f"It is recommended to change from linear search to binary search when m = {m}.")