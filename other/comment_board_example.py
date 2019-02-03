'''Jotting bare idea for how to implement a commenting system'''

class Comment:
    def __init__(self, user, text):
        self.user = user
        self.text = text
        self.replies = []
        
    def __repr__(self):
        return "{0.user} says: {0.text}".format(self)
        

class User:
    def __init__(self, name):
        self.name = name
       
    def __repr__(self):
        return self.name
        
def generate_comment_thread_tree(comment, current_indent_level=0):
    '''this function should implement a recursive call to generate levels of replies to the main thread'''
    print('-'*current_indent_level, comment)
    print()
    if not comment.replies:
        return
    else:
        for reply in comment.replies:
            generate_comment_thread_tree(reply, current_indent_level+4)


foo = User('foo')
bar = User('bar')
baz = User('baz')
baa = User('baa')
fooz = User('fooz')
a = Comment(foo, 'this is a toplevel comment')
b = Comment(bar, 'this is a reply to toplevel comment')
c = Comment(foo, 'this is a reply to comment b')
d = Comment(baz, 'This is a reply to comment b')
e = Comment(fooz, 'This is a reply to toplevel comment')
f = Comment(baa, 'This is a reply to toplevel comment')
g = Comment(foo, 'This is a reply to comment f')
h = Comment(baa, 'This is a reply to comment g')

a.replies.append(b)
a.replies.append(e)
a.replies.append(f)
b.replies.append(c)
b.replies.append(d)
f.replies.append(g)
g.replies.append(h)

generate_comment_thread_tree(a)
