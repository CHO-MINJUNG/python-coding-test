"""N(2≤N≤10,000)개의 섬으로 이루어진 나라가 있다. 이들 중 몇 개의 섬 사이에는 다리가 설치되어 있어서 차들이 다닐 수 있다.

영식 중공업에서는 두 개의 섬에 공장을 세워 두고 물품을 생산하는 일을 하고 있다. 물품을 생산하다 보면 공장에서 다른 공장으로 생산 중이던 물품을 수송해야 할 일이 생기곤 한다. 그런데 각각의 다리마다 중량제한이 있기 때문에 무턱대고 물품을 옮길 순 없다. 만약 중량제한을 초과하는 양의 물품이 다리를 지나게 되면 다리가 무너지게 된다.

한 번의 이동에서 옮길 수 있는 물품들의 중량의 최댓값을 구하는 프로그램을 작성하시오.
"""

import sys
class Node():
    def __init__(self,num):
        self.num= num
        self.link = {}

N, M = sys.stdin.readline().split()
Nodes = []
for j in range(int(N)):
    Nodes.append(Node(j+1))

for _ in range(int(M)):
    A, B, C = map(int, sys.stdin.readline().split())
    if B in Nodes[A-1].link and Nodes[A-1].link[B]<C:
        Nodes[A-1].link[B] = C
    elif B not in Nodes[A-1].link:
        Nodes[A-1].link[B] = C
    if A in Nodes[B-1].link and Nodes[B-1].link[A]<C:
        Nodes[B-1].link[A] = C
    elif A not in Nodes[B-1].link:
        Nodes[B-1].link[A] = C

start, end = sys.stdin.readline().split()
print(Nodes[int(start)-1].link[int(end)])