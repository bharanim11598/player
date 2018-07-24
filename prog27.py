n= input()
i=""
c=""
for i in n:
  if i.isupper():
    c=c+''+i.lower()
  else:
    c=c+''+i.upper()
print(c)
