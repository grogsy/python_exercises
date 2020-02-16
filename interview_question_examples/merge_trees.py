# https://leetcode.com/problems/merge-two-binary-trees/submissions/

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def mergeTrees(t1, t2):
    if t1 and t2:
        this_node = TreeNode(t1.val + t2.val)
        this_node.left = mergeTrees(t1.left, t2.left)
        this_node.right = mergeTrees(t1.right, t2.right)
    else:
        this_node = t1 or t2

    return this_node
