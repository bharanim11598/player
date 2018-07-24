a = int(input())
pf = []
for x in range(2, a):
  while a % x == 0:
    pf.append(x)
    a = a // x
    if a>1:
      print(pf)
