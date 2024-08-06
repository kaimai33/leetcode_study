# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def addToArr(node):
            if not node:
                return
            arr.append(node.val)
            addToArr(node.left)
            addToArr(node.right)
            return
        if not root:
            return 0
        arr = []
        addToArr(root)
        arr.sort()
        ans = float("inf")
        for i in range(1, len(arr)):
            ans = min(ans, arr[i] - arr[i-1])
        return ans
        