# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def populateTree(root, val):
            if not root:
                return
            if val < root.val:
                if not root.left:
                    root.left = TreeNode(val)
                else:
                    populateTree(root.left, val)
            elif val > root.val:
                if not root.right:
                    root.right = TreeNode(val)
                else:
                    populateTree(root.right, val)
            return
        
        if not preorder:
            return None

        ans = TreeNode(preorder[0])
        
        for i in range(1, len(preorder)):
            populateTree(ans, preorder[i])
        return ans
