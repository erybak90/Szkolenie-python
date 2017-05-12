from model.contact import Contact

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.open_add_new_contact_form()
        app.contact.init_fill_contact_form(
            Contact(Firstname="First name", Lastname="Last name", Nickname="NIckname", company="Corpo", adress="Poland",
                    mobile="698998657",
                    email="wcia@radiowy.net", notes="Dodanie kontaktu"))
        app.contact.submit_contact_creation()
    app.contact.delete_first_contact()
