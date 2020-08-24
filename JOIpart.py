import sys
class Node():
    def __init__(self, data):
        self.data = data
        self.condict = {}

N, M, C = list(map(int, sys.stdin.readline().split()))
nodes = [0]*N
distance = []
minnum = 1000000000000000
for i in range(N):
    nodes[i] = Node(i+1)
for i in range(M):
    Ai, Bi, Di = list(map(int, sys.stdin.readline().split()))
    nodes[Ai-1].condict[Bi] = Di
    nodes[Bi-1].condict[Ai] = Di 
    distance.append(Di)

print(distance)
for i in distance:
    sum = 0
    for j in distance:
        if j<=i:
            sum+= (C*i)
        else:
            sum+=j
    if sum<minnum:
        minnum = sum
for i in range(0,min(distance)):
    sum = 0
    for j in distance:
        if j<=i:
            sum+= (C*i)
        else:
            sum+=j
    if sum<minnum:
        minnum = sum


print(minnum)