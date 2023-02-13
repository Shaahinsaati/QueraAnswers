vorodi = input()
counter=0
if vorodi.isnumeric():
    for item in range(1,int(vorodi)):
        if int(vorodi)%item==0:
            counter+=item
    if(int(vorodi)==counter):
        print("YES")
    else:
        print("NO")
else:
    print("Invalid input!")