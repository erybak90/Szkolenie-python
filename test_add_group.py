# -*- coding: utf-8 -*-
import unittest
import pytest
from group import Group
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

    def test_add_group(self):
        app.login(username="admin", password="secret")
        app.create_group(Group(name="Nowe 1 zadanie", header="Nowe zadanie", footer="Nowe zadanie"))
        app.logout()

    def test_add__empty_group(self):
        app.login(username="admin", password="secret")
        app.create_group(Group(name="", header="", footer=""))
        app.logout()

