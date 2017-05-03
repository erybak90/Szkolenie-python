# -*- coding: utf-8 -*-
from model.group import Group



def test_add_group(app):
    app.group.create(Group(name="Nowe 1 zadanie", header="Nowe zadanie", footer="Nowe zadanie"))

def test_add__empty_group(app):
    app.group.create(Group(name="", header="", footer=""))