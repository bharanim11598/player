n= int(input())
rev=0
m=0
while(n>0):
  rem=n%10
  rev=((rev*10)+rem)
  m=m+rem**2
  n=n//10
  
print(m)
  
