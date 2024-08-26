"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ans = []
        def traverse(node):
            if not node:
                return
            elif not node.children:
                ans.append(node.val)
            else:
                for child in node.children:
                    traverse(child)
                ans.append(node.val)
        traverse(root)
        return ans