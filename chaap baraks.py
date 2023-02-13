listOfNumbers = []
while True:
    i = int(input())
    if i == 0:
        break
    else:
        listOfNumbers.append(i)
for i in listOfNumbers[::-1]:
    print(i)