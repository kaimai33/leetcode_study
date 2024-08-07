# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def rec(root, curr_length, direction):
            nonlocal ans
            if not root:
                return
            ans = max(ans, curr_length)

            if direction == "left":
                rec(root.left, curr_length + 1, "right")
                rec(root.right, 1, "left")
            elif direction == "right":
                rec(root.right, curr_length + 1, "left")
                rec(root.left, 1, "right")
        
        ans = 0
        rec(root, 0, "left")
        rec(root, 0, "right")
        return ans
        