import sys
class Node():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
def search(actnum, node):
    if node.data == actnum:
        return node
    else:
        if node.left != None:
            search(actnum, node.left)
        elif node.right != None:
            search(actnum, node.right)

      
for i in range(int(sys.stdin.readline())):
    nodes = sys.stdin.readline().split()
    for j in range(3):
        if nodes[j] == ".":
            nodes[j]=None
    if i==0:
        tree = Node(nodes[0])
        tree.left = Node(nodes[1])
        tree.right = Node(nodes[2])
    else:
        node = search(nodes[0],tree)
        node.left = Node(nodes[1])
        node.right = Node(nodes[2])

print(tree.data, tree.left.data, tree.right.data, tree.left.left.data)
    