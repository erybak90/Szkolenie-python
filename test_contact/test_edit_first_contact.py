from model.contact import Contact


def test_modify_contact_firstname(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(Firstname="New firstname"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


#def test_modify_contact_nickname(app):
#    old_contacts = app.contact.get_contact_list()
#    app.contact.modify_first_contact(Contact(Nickname="New nickname"))
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)