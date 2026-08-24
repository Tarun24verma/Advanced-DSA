class Node:
    def __init__(self, data):
        self.val=data
        self.left=None
        self.right=None
    def __repr__(self):
        return str(self.val)

node1=Node(1)
node2=Node(2)
node3=Node(4)
node4=Node(5)
node5=Node(3)
node6=Node(6)
node1.left=node2
node1.right=node5
node2.left=node3
node2.right=node4
node5.right=node6
def lca(root,p,q):
    if root is None:
        return None
    if root.val == p or root.val==q:
        return root
    left=lca(root.left,p,q)
    right=lca(root.right,p,q)
    if left and right:
        return root
    return left if left else right

ac=lca(node1,4,5)
