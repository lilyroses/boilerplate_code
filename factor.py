# factor.py
import math


def factor(x):
    factors = []
    y = math.ceil(math.sqrt(x))
    for i in range(2, y+1):
        if x % i == 0:
            factors.append(i)
    print(f"Factors of {x}:")
    print(factors)


if __name__ == "__main__":
    x = int(input("x: "))
    factor(x)
