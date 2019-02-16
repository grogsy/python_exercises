def is_palindrome(node):
    '''Needs to be tested, this is just a scratch note of how i would implement a palindrome checker using linked list facilities'''
    
    left = right = node
    # Get tail to its proper starting position
    while right.next is not None:
        right = right.next
        
    
    # head count
    i = 0
    # tail count
    j = node.count()
    
    # with this, it should work for either even or odd numbered strings
    while i < j or i == j:
        # compare the data at each seeking node
        if left.data != right.data:
            return False
        i += 1
        left = left.next
        j -= 1
        right = right.prev
        
    return True
