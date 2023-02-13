from math import pow
n=input()
if n.isnumeric():
    n=int(n)
    c=0
    for i in range(0,n):
        if pow(2, i)>n:
            c+=pow(2,i)
            break
    print(int(c))