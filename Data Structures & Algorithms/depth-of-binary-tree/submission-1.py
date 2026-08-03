# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        if root.left is not None:
            left_depth = self.maxDepth(root.left)
        else:
            left_depth = 0
        
        if root.right is not None:
            right_depth = self.maxDepth(root.right)
        else:
            right_depth = 0
        
        return max(left_depth+1, right_depth+1)
        