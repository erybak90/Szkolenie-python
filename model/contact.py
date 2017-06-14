from sys import maxsize
class Contact:
    def __init__(self, Firstname=None, Lastname=None, Nickname=None, company=None, homephone=None, mobilephone=None, workphone=None, secondaryphone=None, id=None):
        self.Firstname = Firstname
        self.Lastname = Lastname
        self.Nickname = Nickname
        self.company = company
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.Firstname, self.Lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id)\
            and self.Firstname == other.Firstname and self.Lastname == other.Lastname


    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
