# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        levels = []
        def rec(root, lvl):
            if not root:
                return
            if len(levels) == lvl:
                levels.append([])
            levels[lvl].append(root.val)
            rec(root.left, lvl + 1)
            rec(root.right, lvl + 1)
            
        rec(root, 0)
        for level in levels:
            ans.append(sum(level) / len(level))

        return ans
            