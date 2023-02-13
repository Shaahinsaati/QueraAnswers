#Why shoud we use while statement? because of a condition that final number must be less than ten
n = input()
while len(n)!=1:
    s = 0
    for i in n:
        s+=int(i)
    n = str(s)
print(n)