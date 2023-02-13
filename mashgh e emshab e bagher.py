def Checktriangle(a,b,c):
    return True if a+b+c==180 and a!=0 and b!=0 and c!=0 else False
# fa-> First angle , sa -> second angle , tha-> third angle
inp=(input().split())
fa,sa,tha=float(inp[0]),float(inp[1]),float(inp[2])
print('Yes')if Checktriangle(fa,sa,tha) else print('No')
