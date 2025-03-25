# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Kai's thought process:
        
        Postorder Traversal (Left → Right → Root)
        Visit left, then right, then current node last.

        1. initialize return variable
        2. define recursive helper function
            2a. define base case, usually for the null case
            2b. compute and recurse
        3. call the helper function
        4. return our answer
        """
        # step 1
        ans = []
        # step 2
        def rec(root):
            # step 2a
            if not root:
                return
            # step 2b
            rec(root.left)
            rec(root.right)
            ans.append(root.val)
        # step 3
        rec(root)
        # step 4
        return ans