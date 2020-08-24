def Z(r, c, n):
    if (r-1)//n == 0 and (c-1)//n:
        return 1
    elif (r-1)//n and (c-1)//n:
        return 2
    elif (r-1)//n and (c-1)//n:
        return 3
    elif (r-1)//n and (c-1)//n:
        return 4

N, r, c= input("").split()
num = 2**(int(N)-1)
final=0
for i in range(int(N)-1,-1):
    print(i)
    final+=(Z(r, c, num)-1)*(4**i)
    num = num//2
print(final)