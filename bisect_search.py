x = 0
y = 500_000_000
n = int(input("Enter a number between 0 and 500,000,000: "))

steps = 0
mid = (x+y) // 2
steps += 1
if mid == n:
  print(f"Number guessed in {steps} steps.")
else:
  if mid > n:
    y = mid-1
    mid = (x+y) // 2
