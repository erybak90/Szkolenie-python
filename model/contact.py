
from sys import maxsize
class Contact:
    def __init__(self, Firstname=None, Lastname=None, Nickname=None, company=None, address=None, mobile=None, email=None, notes=None):
        self.Firstname = Firstname
        self.Lastname = Lastname
        self.Nickname = Nickname
        self.company = company
        self.address = address
        self.mobile = mobile
        self.email = email
        self.notes = notes
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.Firstname, self.Lastname)

    def __eq__(self, other):
        return self.Firstname == other.Firstname and self.Lastname == other.Lastname

