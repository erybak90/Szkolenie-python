
def test_delete_first_contact(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.group.delete_first_contact()
    app.session.logout()