# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/submissions/

from itertools import chain

def dfs(node, digitArr, currentDigit):
    digit = currentDigit + str(node.val)

    if node.left:
        digitArr = dfs(node.left, digitArr, digit)
    if node.right:
        digitArr = dfs(node.right, digitArr, digit)
    if not node.left and not node.right:
        digitArr.append(digit)

    return digitArr
    
def sumRootToLeaf(root):
        if not root.left and not root.right:
            return root.val
        
        numsLeft = []
        numsRight = []
        
        if root.left:
            numsLeft = dfs(root.left, digitArr=numsLeft, currentDigit=str(root.val))
        if root.right:
            numsRight = dfs(root.right, digitArr=numsRight, currentDigit=str(root.val))
        
            
        return sum(int(binaryNum, 2) for binaryNum in chain(numsLeft, numsRight))
