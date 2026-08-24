class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

node1=Node(8)
node2=Node(10)
node3=Node(11)
node4=Node(15)
node5=Node(2)
node6=Node(4)
node7=Node(3)
node1.right=node2
node1.left=node3
node3.left=node4
node3.right=node5
node2.left=node6
node2.right=node7

# def print_tree(root):
#     if root:
#         print(root.data)
#         print_tree(root.left)
#         print_tree(root.right)
#     return None

# def print_tree(root):
#     if root:
#         print_tree(root.left)
#         print(root.data)
#         print_tree(root.right)
#     return None

def print_tree(root):
    if root:
        print_tree(root.left)
        print_tree(root.right)
        print(root.data)
    return None

print_tree(node1)

def search_tree(root, k):
    if root is None:
        return None
    if root.data==k:
        return "Result Found!"
    result = search_tree(root.left,k)
    if result:
        return result
    return search_tree(root.right, k)

print(search_tree(node1, 10))
