# https://leetcode.com/problems/maximum-depth-of-binary-tree/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def maxDepth(root):
  def dfs(node, count):
    if not node:
        return count
    elif not node.left:
        return dfs(node.right, count + 1)
    elif not node.right:
        return dfs(node.left, count + 1)
    else:
        left_count = dfs(node.left, count + 1)
        right_count = dfs(node.right, count + 1)
        return max(left_count, right_count)
        
  return dfs(root, 0)
