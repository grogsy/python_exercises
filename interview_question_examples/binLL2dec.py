# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

def getDecimalValue(head):
    def recurse(node):
        if not node.next:
            accumulative = node.val
            return 1, accumulative

        weight, accumulative =  recurse(node.next)

        weight <<= 1

        accumulative += weight * node.val

        return weight, accumulative


    weight, accumulative = recurse(head)

    return accumulative
