from model.contact import Contact
from random import randrange


def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact(Contact(Firstname="First name", Lastname="Last name", address="NIckname", address2="Corpo", home="Poland",
                mobile="698998657",
                work="wcia@radiowy.net", phone2="Dodanie kontaktu"))
    old_contacts = app.contact.get_contact_list()
    index = randrange (len(old_contacts))
    app.contact.modify_contact_by_index(index, Contact(Firstname="New firstname"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)



#def test_modify_contact_nickname(app):
#    old_contacts = app.contact.get_contact_list()
#    app.contact.modify_first_contact(Contact(Nickname="New nickname"))
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)