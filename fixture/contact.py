from model.contact import Contact
class ContactHelper:

    def __init__(self, app):
        self.app = app


    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.select_contact_by_index(index)
        # open modification form
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        # fill contact form
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element_by_name("update").click()
        wd.find_element_by_link_text("home").click()
        self.contact_cache = None

    def modify_first_contact(self):
        self.modify_contact_by_index(0)


    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_link_text("home").click()
        self.contact_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def submit_contact_creation(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        wd.find_element_by_link_text("home").click()
        self.contact_cache = None

    def init_fill_contact_form(self, contact):
        wd = self.app.wd
        # init contact creation
        self.fill_contact_form(contact)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.Firstname)
        self.change_field_value("lastname", contact.Lastname)
        self.change_field_value("nickname", contact.Nickname)
        self.change_field_value("company", contact.company)
        self.change_field_value("homephone", contact.homephone)
        self.change_field_value("mobilephone", contact.mobilephone)
        self.change_field_value("workphone", contact.workphone)
        self.change_field_value("secondaryphone", contact.secondaryphone)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def open_add_new_contact_form(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                Firstname = cells [1].text
                Lastname = cells [2].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                all_phones = cells[5].text.splitlines()
                self.contact_cache.append(Contact(Firstname=Firstname, Lastname=Lastname, id=id,
                                                  homephone=all_phones[0], mobilephone=all_phones[1],
                                                  workphone=all_phones[2], secondaryphone=all_phones[3]))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()


    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        Firstname = wd.fin_element_by_name("firstname").get_attribute("value")
        Lastname = wd.fin_element_by_name("lastname").get_attribute("value")
        id = wd.fin_element_by_name("id").get_attribute("value")
        homephone = wd.fin_element_by_name("home").get_attribute("value")
        mobilephone = wd.fin_element_by_name("mobile").get_attribute("value")
        workphone = wd.fin_element_by_name("work").get_attribute("value")
        secondaryphone = wd.fin_element_by_name("phone2").get_attribute("value")
        return Contact(Firstname=Firstname, Lastname=Lastname, id = id,
                       homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, secondaryphone=secondaryphone)