from model.contact import Contact


def test_modify_contact_firstname(app):
    app.contact.modify_first_contact(Contact(Firstname="New firstname"))


def test_modify_contact_nickname(app):
    app.contact.modify_first_contact(Contact(Nickname="New nickname"))