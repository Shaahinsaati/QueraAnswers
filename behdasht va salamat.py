x = int(input())
n = int(input())
if n == 0:
    print('20')
elif n == 7:
    print(x)
elif n < x:
    print(x-n)
elif x-n <= 0:
    print('0')