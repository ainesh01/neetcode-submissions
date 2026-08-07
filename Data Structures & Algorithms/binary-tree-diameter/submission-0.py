# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = 0
        def getDia(root: Optional[TreeNode]) -> int:
            if root == None:
                return 0
            leftLen = getDia(root.left)
            rightLen = getDia(root.right)
            maxDiameter = max(maxDiameter, leftLen+rightLen)
            return max(leftLen, rightLen)
        getDia( root)
