from model.contact import Contact
from random import randrange


def test_modify_some_contact(app):
    if app.contact.count() == 0:
        app.contact(Contact(Firstname="First name", Lastname="Last name", homephone="NIckname", mobilephone="Corpo",
                            address="Poland",
                            workphone="698998657",
                            email="wcia@radiowy.net", email2="Dodanie kontaktu"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(Firstname="new")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, Contact())
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


#def test_modify_contact_nickname(app):
#    old_contacts = app.contact.get_contact_list()
#    app.contact.modify_first_contact(Contact(Nickname="New nickname"))
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)