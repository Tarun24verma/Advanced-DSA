class BST_Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
root=BST_Node(10)
root.left=BST_Node(5)
root.right=BST_Node(15)
root.left.left=BST_Node(3)
root.left.right=BST_Node(7)
root.right.right=BST_Node(18)
low=7; high=15
s=0
def sum(root):
    global s
    if root:
        if root.val<=low:
            if root.val<low:
                return sum(root.right)
            else:
                s+=root.val
                return sum(root.right)
        elif root.val>=high:
            if root.val>high:
                return sum(root.left)
            else:
                s+=root.val
                return sum(root.left)
        else:
            s+=root.val
            sum(root.right)
            sum(root.left)
    else:
        return None

sum(root)
print(s)



"""---Leet Code Solution---
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root: return 0
        if root.val>high: return self.rangeSumBST(root.left, low, high)
        if root.val<low: return self.rangeSumBST(root.right, low, high)
        return root.val + self.rangeSumBST(root.left,low,high) + self.rangeSumBST(root.right,low,high)"""
