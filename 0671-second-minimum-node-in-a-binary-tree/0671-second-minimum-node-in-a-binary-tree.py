# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        arr = set()
        tgt = root.val
        def rec(root):
            if not root:
                return
            arr.add(root.val)
            rec(root.left)
            rec(root.right)
        rec(root)
        arr = sorted(arr)
        for val in arr:
            if val != tgt:
                return val
        return -1

        
        