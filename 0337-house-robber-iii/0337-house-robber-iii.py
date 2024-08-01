# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        """
        Thought process:
        1. I wrote down the answer from online.. I should review this later
        """ 

        def dfs(root):
            if not root:
                return (0, 0)

            left = dfs(root.left)
            right = dfs(root.right)

            rob = root.val + left[1] + right[1] # we rob the current val and do not rob the children
            no_rob = max(left) + max(right) # doesn't include curr val

            return (rob, no_rob)
        
        return max(dfs(root))
     