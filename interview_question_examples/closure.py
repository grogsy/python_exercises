def secret_people(people_list, secret):
    def mask(guest):
        def validate(secret_code):
            return guest if secret_code == secret else "invalid code"
        return validate
        
    return [mask(guest) for guest in people_list]
    
    
ppl = 'me you them'.split(' ')

secret_list = secret_people(ppl, 512)

# every item is a function object
print(secret_list)

# returns "invalid code"
for s in secret_list:
    print(s(513))
    
# returns items from list ppl
for s in secret_list:
    print(s(512))
