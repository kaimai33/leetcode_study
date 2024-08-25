# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        arr = []
        def convToArr(root, level):
            if not root:
                return
            if level == len(arr):
                arr.append([])
            arr[level].append(root.val)
            convToArr(root.left, level + 1)
            convToArr(root.right, level + 1)

        convToArr(root, 0)
        for i in range(1, len(arr), 2):
            arr[i].reverse()


        def changeTree(root, level):
            if not root:
                return
            root.val = arr[level].pop(0)
            changeTree(root.left, level + 1)
            changeTree(root.right, level + 1)
        changeTree(root, 0)
        return root
            