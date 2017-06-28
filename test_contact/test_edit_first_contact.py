from model.contact import Contact
from random import randrange


def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact(Contact(Firstname="First name", Lastname="Last name", homephone="NIckname", mobilephone="Corpo",
                            address="Poland",
                            workphone="698998657",
                            email="wcia@radiowy.net", email2="Dodanie kontaktu"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.modify_contact_by_index(index, Contact(Firstname="New firstname"))
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = old_contacts
    assert len(old_contacts) == len(new_contacts)
    assert old_contacts == new_contacts


#def test_modify_contact_nickname(app):
#    old_contacts = app.contact.get_contact_list()
#    app.contact.modify_first_contact(Contact(Nickname="New nickname"))
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)