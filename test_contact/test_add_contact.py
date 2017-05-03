# -*- coding: utf-8 -*-

from model_contact.contact import Contact


def test_add_contact(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.open_add_new_contact_form()
    app.contact.init_fill_contact_form(
        Contact(Firstname="First name", Lastname="Last name", Nickname="NIckname", company="Corpo", adress="Poland",
                mobile="698998657",
                email="wcia@radiowy.net", notes="Dodanie kontaktu"))
    app.contact.submit_contact_creation()
    app.session.logout()


def test_add_empty_contact(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.open_add_new_contact_form()
    app.contact.init_fill_contact_form(Contact(Firstname="", Lastname="", Nickname="", company="", adress="", mobile="",
                                       email="", notes=""))
    app.contact.submit_contact_creation()
    app.session.logout()
