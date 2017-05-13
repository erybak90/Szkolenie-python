# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    app.contact.open_add_new_contact_form()
    app.contact.init_fill_contact_form(Contact(Firstname="First name", Lastname="Last name", Nickname="NIckname", company="Corpo", address="Poland",
                mobile="698998657",
                email="wcia@radiowy.net", notes="Dodanie kontaktu"))
    app.contact.submit_contact_creation()



def test_add_empty_contact(app):
    app.contact.open_add_new_contact_form()
    app.contact.init_fill_contact_form(Contact(Firstname="", Lastname="", Nickname="", company="", address="", mobile="", email="", notes=""))
    app.contact.submit_contact_creation()

