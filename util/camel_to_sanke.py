def camel_to_snake(camel_word):
    
    out = [camel_word[0].lower()]
    
    for c in camel_word[1:]:
        if c.isupper():
            out.append('_')
            out.append(c.lower())
        else:
            out.append(c)
            
    return ''.join(out)
