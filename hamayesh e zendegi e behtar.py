inputs=[int(x) for x in input().split(' ')]
r=inputs[0]
c = inputs[1]
if 1<=r<=10 and 1<=c<=10:
    r = (10-r)+1
    print('Right %i %i'%(r,c))
else:
    r = (10-r)+1
    c = (20-c)+1
    print('Left %i %i'%(r,c))