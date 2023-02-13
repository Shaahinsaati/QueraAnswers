vorodi1 = input()
vorodi2 = input()

if vorodi1.isnumeric() and vorodi2.isnumeric() and int(vorodi2)!=0:
    for item in range(int(vorodi1),int(vorodi2)+1):
        if item>1:
            for each in range(2,item):
                if (item%each)==0:
                    break
            else:
                print(item)