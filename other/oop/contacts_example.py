'''demonstrates inheritance and multiple inheritance'''

class Contact:
    all_contacts = []
    def __init__(self, name='', email='', **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.email = email
        self.all_contacts.append(self)

    def __repr__(self):
        # using a dict to test dict interpolation with old-style formatting
        info = dict(name=self.name,
                    email=self.email)
        # return "%(name)s: %(email)s" % info
        return "Contact<%(name)s>" % info

class AddressHolder:
    def __init__(self, street='', city='', state='', code='', **kwargs):
        super().__init__(**kwargs)
        self.street = street
        self.city = city
        self.state = state
        self.code = code

class Friend(Contact, AddressHolder):
    def __init__(self, phone='', **kwargs):
        super().__init__(**kwargs)
        self.phone = phone

    def __repr__(self):
        return "Friend<%s>" % self.name




# Interfaces to creating new objects
def make_contact(friend=False):
    info = dict(name=input('name: '),
                email=input('email: '))

    return Contact(**info)


def make_friend():
    info = dict(name=input('name: '),
                email=input('email: '),
                phone=input('phone number: '),
                street=input('street: '),
                city=input('city: '),
                state=input('state: '),
                code=input('zip code: '))
    return Friend(**info)

