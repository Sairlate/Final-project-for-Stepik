from pages.login_page import LoginPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/accounts/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()


def test_guest_can_go_to_login_pag(browser):
    link = "http://selenium1py.pythonanywhere.com/accounts/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()


def test_guest_can_go_to_login_pa(browser):
    link = "http://selenium1py.pythonanywhere.com/accounts/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()