# factorial.py

def factorial(n):
  x = n
  while n > 2:
    n -= 1
    x *= n
  return x


if __name__ == "__main__":
  n = int(input("n: "))
  print(factorial(n))
