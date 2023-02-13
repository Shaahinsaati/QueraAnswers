number = (input()).split(" ")
a,b,l = map(int,number)
sums = 0
for i in range(1, l + 1):
    sums +=a if i % 2 != 0 else b
    # if i % 2 != 0:
    #     sums += a
    # else:
    #     sums += b

print(sums)