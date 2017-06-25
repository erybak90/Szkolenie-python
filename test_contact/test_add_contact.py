from model.contact import Contact

def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(Firstname="Firstname", Lastname="Lastname", address="Address",
                      homephone="000000000", mobilephone="698998657",
                workphone="555588888", secondaryphone="888889999", email="xyz@onet.pl", email2="abc@abc.pl", email3="jkl@ok.pl")
    app.contact.open_add_new_contact_form()
    app.contact.init_fill_contact_form(contact)
    app.contact.submit_contact_creation()
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()


#def test_add_empty_contact(app):
#    old_contacts = app.contact.get_contact_list()
#    contact = Contact(Firstname="", Lastname="", Nickname="", company="", address="", mobile="", email="", notes="")
#    app.contact.open_add_new_contact_form()
#    app.contact.init_fill_contact_form(contact)
#    app.contact.submit_contact_creation()
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) + 1 == len(new_contacts)

