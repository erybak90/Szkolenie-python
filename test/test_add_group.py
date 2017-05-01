# -*- coding: utf-8 -*-
from model.group import Group





def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="Nowe 1 zadanie", header="Nowe zadanie", footer="Nowe zadanie"))
    app.session.logout()

def test_add__empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()