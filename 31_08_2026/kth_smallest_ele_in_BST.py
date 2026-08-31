# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        t=[]
        def it(root):
            if not root or len(t)==k:
                return
            it(root.left)
            t.append(root.val)
            it(root.right)
        it(root)
        return t[k-1]