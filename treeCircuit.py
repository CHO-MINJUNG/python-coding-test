import sys
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class Tree:
    def __init__(self):
        self.root = None
    def makeRoot(self, node, left_node, right_node):
        if self.root == None:
            self.root = node
        if left_node.data != None:
            node.left = left_node
        if right_node.data != None:
            node.right = right_node
    def nodeSearch(self, node, data):
        if not node == None:
            if node.data == data:
                return node
        if not node.left == None:
            self.nodeSearch(node.left,data)
        if not node.right == None:
            self.nodeSearch(node.right, data)
    def preorderTraversal(self, node):
        print(node, end='')
        if not node.left  == None : self.preorderTraversal(node.left)
        if not node.right == None : self.preorderTraversal(node.right)

    def inorderTraversal(self, node):
        if not node.left  == None : self.inorderTraversal(node.left)
        print(node, end='')
        if not node.right == None : self.inorderTraversal(node.right)

    def postorderTraversal(self, node):
        if not node.left  == None : self.postorderTraversal(node.left)
        if not node.right == None : self.postorderTraversal(node.right)
        print(node, end='')        
TreeNode = Tree()
for i in range(int(sys.stdin.readline())):
    tree = sys.stdin.readline().split()
    for j in range(len(tree)):
        if tree[j] == ".":
            tree[j] = None
    if TreeNode.root == None:
        Treeroot = Node(tree[0])
        TreeNode.makeRoot(Treeroot,Node(tree[1]),Node(tree[2]))
    else:
        newNode = TreeNode.nodeSearch(Treeroot,tree[0])
        TreeNode.makeRoot(newNode, Node(tree[1]), Node(tree[2]))
TreeNode.preorderTraversal(Treeroot)
