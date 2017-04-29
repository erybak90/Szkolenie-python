# -*- coding: utf-8 -*-
import pytest

from fixture_contact.application1 import Application1
from model_contact.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application1()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.open_add_new_contact_form()
    app.init_fill_contact_form(
        Contact(Firstname="First name", Lastname="Last name", Nickname="NIckname", company="Corpo", adress="Poland",
                mobile="698998657",
                email="wcia@radiowy.net", notes="Dodanie kontaktu"))
    app.submit_contact_creation()
    app.session.logout()


def test_add_empty_contact(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.open_add_new_contact_form()
    app.init_fill_contact_form(Contact(Firstname="", Lastname="", Nickname="", company="", adress="", mobile="",
                                       email="", notes=""))
    app.submit_contact_creation()
    app.session.logout()
