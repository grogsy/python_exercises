# https://leetcode.com/problems/invert-binary-tree/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def invertTree(root: TreeNode) -> TreeNode:
    if not root or (not root.left and not root.right):
        return root

    self.invertTree(root.left)
    self.invertTree(root.right)

    root.left, root.right = root.right, root.left

    return root
