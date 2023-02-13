x1, y1, x2, y2 = map(int,input().strip().split(' '))
if 1 <= x1 <= 100 and 1 <= y1 <= 100 and 1 <= x2 <= 100 and 1 <= y2 <= 100:
    if y1 == y2 :
        print('Horizontal')
    elif x1 == x2 :
        print('Vertical')
    else:
        print('Try again')