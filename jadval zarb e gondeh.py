n=int(input())
if n>=1 and n<=100:
    for i in range(1,n+1):
        for j in range(1,n+1):
            print(i*j,end=' ')
        print('\n')