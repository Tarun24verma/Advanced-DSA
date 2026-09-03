# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root):
        last_sum=0
        def t(root):
            nonlocal last_sum
            if not root:
                return
            t(root.right)
            temp=last_sum
            last_sum+=root.val
            root.val+=temp
            t(root.left)
        t(root)
        return root