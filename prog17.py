a=int(input())
b=int(input())
if(a>b):
    n1=a
else:
    n2=b
while(1):
    if(n1%a==0 and n1%b==0):
        print(n1)
        break
    n1=n1+1
