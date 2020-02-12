# https://leetcode.com/problems/symmetric-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def isSymmetric(root):
    if not root or (not root.left and not root.right):
        return True

    if (root.left and not root.right) or (root.right and not root.left):
        return False

    q = [root.left, root.right]
    while q:
        i = 0
        j = len(q) - 1

        while i < j:
            if q[i]:
                left_val = q[i].val
            else:
                left_val = q[i]

            if q[j]:
                right_val = q[j].val
            else:
                right_val = q[j]
 
            if left_val != right_val:
                return False

            i += 1
            j -= 1

        new_q = []
        while q:
            node = q.pop()

            if node:
                new_q.append(node.left)
                new_q.append(node.right)

        q = new_q

    return True
