# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def build(i, j):
            if i > j:
                return
            max_val = max(nums[i:j+1])
            max_idx = nums.index(max_val)
            root = TreeNode(max_val)
            root.left = build(i, max_idx-1)
            root.right = build(max_idx + 1, j)
            return root
        return build(0, len(nums) - 1)

        