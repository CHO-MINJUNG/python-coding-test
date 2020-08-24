M, N, Q = input("").split()
A = input("")
A = A.split()
if type(A)!=list:
    A = list(A)
A=list(map(int,A))
B = input("")
B = B.split()
full_list = A[:]
for i in range(int(M)-int(N)):
    maxnum=0
    num=None
    if maxnum<A[0]-1:
        maxnum=A[0]-1
        num=A[0]//2
    if len(A)>1:
        for j in range(1,len(A)):
            if maxnum<A[j]-A[j-1]-1:
                maxnum = A[j]-A[j-1]-1
                if maxnum%2 ==0:
                    num = maxnum//2 + A[j-1]
                else:
                    num = maxnum//2 + A[j-1]+1
    if maxnum<int(M)-A[len(A)-1]:
        maxnum=int(M)-A[len(A)-1]
        num=maxnum//2 +1 + A[len(A)-1]   
    full_list.append(num)
    A.append(num)
    A.sort()
print(full_list)
for i in B:
    print(full_list[int(i)-1])