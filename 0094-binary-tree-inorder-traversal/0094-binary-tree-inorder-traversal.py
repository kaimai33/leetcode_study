# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Kai's thought process:
        
        Inorder Traversal: (Left → Root → Right)
        Go to the left first, then visit current node, then right.

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
            ans.append(root.val)
            rec(root.right)
        # step 3
        rec(root)
        # step 4
        return ans


       
