# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if root is None:
            return root
        
        if root.right is None and root.left is None:
            return root
        
        if root.right is None:
            root.right = self.invertTree(root.left)
            root.left = None
            return root
        
        elif root.left is None:
            root.left = self.invertTree(root.right)
            root.right = None
            return root
        
        temp = self.invertTree(root.right)
        root.right = self.invertTree(root.left)
        root.left = temp
        
        return root

