from math import floor 
n,k = map(int,input().split())
for i in range(k):
    n =n/2
print(floor(n))