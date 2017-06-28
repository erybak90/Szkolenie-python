
from model.contact import Contact


def test_add_contact(app, json_contacts):
    contact = json_contacts
    old_contacts = app.contact.get_contact_list()
    app.contact.open_add_new_contact_form()
    app.contact.init_fill_contact_form(contact)
    app.contact.submit_contact_creation()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
