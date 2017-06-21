from sys import maxsize
class Contact:
    def __init__(self, Firstname=None, Lastname=None, address=None, address2=None, all_address_from_home_page=None,
                 home=None, mobile=None, work=None, phone2=None, all_phones_from_home_page=None,
                 id=None, email=None, email2=None, email3=None, all_emails_from_home_page=None):
        self.Firstname = Firstname
        self.Lastname = Lastname
        self.address = address
        self.address2 = address2
        self.home = home
        self.mobile = mobile
        self.work = work
        self.phone2 = phone2
        self.id = id
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_address_from_home_page = all_address_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page

    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s" % (self.Firstname, self.Lastname, self.address, self.home,
                                                     self.mobile, self.email)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id)\
            and self.Firstname == other.Firstname and self.Lastname == other.Lastname


    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
