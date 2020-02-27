# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

from queue import deque

def popleft(q):
    return q.popleft()

def pop(q):
    return q.pop()

def zigzagLevelOrder(root):
    if not root:
        return []

    alternate = False

    q = deque([root])
    output = []

    pop_helper = popleft

    while q:
        temp = deque()
        while q:
            temp.append(pop_helper(q))

        children = deque()
        output_vals = []

        while temp:
            node = temp.popleft()
            output_vals.append(node.val)
            if alternate:
                if node.right:
                    children.appendleft(node.right)
                if node.left:
                    children.appendleft(node.left)
            else:
                if node.left:
                    children.append(node.left)
                if node.right:
                    children.append(node.right)

        q.extend(children)
        output.append(output_vals)
        alternate = not alternate
        
        if alternate:
            pop_helper = pop
        else:
            pop_helper = popleft

    return output
