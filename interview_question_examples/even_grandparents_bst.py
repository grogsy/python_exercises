# https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent

def dfs(node, ancestors):
    count = 0
    if len(ancestors) >= 2 and ancestors[-2] % 2 == 0:
        count += node.val

    if node.left:
        count += dfs(node.left, ancestors + [node.val])
    if node.right:
        count += dfs(node.right, ancestors + [node.val])

    return count

def sumEvenGrandparent(root):
    if not root:
        return 0
    return dfs(root, [])
