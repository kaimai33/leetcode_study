# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        # cache
        cache = {
            0: [],
            1: [TreeNode()]
        }

        def dfs(n):
            if n in cache:
                return cache[n]

            res = []
            for l in range(n):
                r = n - 1 - l
                # leftTrees is a list of all FBTs you can make
                leftTrees, rightTrees = dfs(l), dfs(r)

                # we iterate through all possible combos of FBTs
                for t1 in leftTrees:
                    for t2 in rightTrees:
                        res.append(TreeNode(0, t1, t2))
            cache[n] = res
            return res
        
        return dfs(n)

