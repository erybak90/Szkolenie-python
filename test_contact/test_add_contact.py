
from model.contact import Contact
import pytest
import random
import string
from data.add_contact import constant as testdata

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    pass
    old_contacts = app.contact.get_contact_list()
    app.contact.open_add_new_contact_form()
    app.contact.init_fill_contact_form(contact)
    app.contact.submit_contact_creation()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    sorted(old_contacts + [contact], key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
