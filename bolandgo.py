n = input()
if 1 <= len(n) <= 20:
    for i in range(0,len(n)):
        print(i*n[i]+n[i:])