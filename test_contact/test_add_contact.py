# -*- coding: utf-8 -*-

from model.contact import Contact
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols)for i in range(random.randrange(maxlen))])


testdata = [Contact(Firstname="", Lastname="",address="", address2="", home="", mobile=random_string("666", 6),
                work="", phone2="", email="", email2="", email3="")] + [
        Contact(Firstname=random_string("first", 10), Lastname=random_string("last", 10),
                address=random_string("address", 10), address2=random_string("address2", 10),
                home=random_string("92", 7), mobile=random_string("666", 6),
                work=random_string("0", 8), phone2=random_string("0000", 5), email=random_string("abc", 5),
                email2=random_string("zxc", 5), email3=random_string("ghjk", 5)) for i in range (5)


    ]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    pass
    old_contacts = app.contact.get_contact_list()
    app.contact.open_add_new_contact_form()
    app.contact.init_fill_contact_form(contact)
    app.contact.submit_contact_creation()
    assert len(old_contacts) + 1 == app.contact.count()


