x = 100

allocs = []

a = 0
b = 0
c = x

alloc = [a,b,c]
allocs.append(alloc)


while c > 0:
  c -= 1
  b += 1
  alloc = [a,b,c]
  allocs.append(alloc)
  if c == 0:
    b = 0
    
    while a < x:
      a += 1

      c = x- (a+b)



for a in allocs:
  print(a)
