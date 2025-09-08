from factorial import factorial as factorial

def num_combos(n, k):
  # n is number of items, k is length of combination
  # n! / k! * (n-k)!
  return int(factorial(n) / (factorial(k) * (factorial(n-k))))


if __name__ == "__main__":
  n = int(input("n: "))
  k = int(input("k: "))
  print("num combos: ", num_combos(n, k))
