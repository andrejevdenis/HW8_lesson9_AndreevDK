from Pages.resources import RegistrationPage
from Pages.assert_res import Assert_results
from data.users import test_user


def test_complete_todo(browser_management):
    registration_page = RegistrationPage

    # Шаги выполнения
    registration_page.register(test_user)
    # Проверки
    Assert_results.in_submit_form(test_user)