from resources.resources import RegistrationPage
from resources.assert_res import Assert_results

def test_complete_todo(browser_management):
    # Шаги выполнения
    registration_page = RegistrationPage

    registration_page.fill_first_name('Fedor')
    registration_page.fill_last_name('Lomovoy')
    registration_page.fill_email('fedyaosminog@ramb.com')
    registration_page.fill_gender('Other')
    registration_page.fill_mobile_num('1000000000')
    registration_page.fill_date_of_birth('9', '2000', '23')
    registration_page.add_subject('Maths').add_subject('Computer Science') #Для добавления дополнительного субъекта продолжить добавлене класса ".add_subject", наименование указывать полностью, регистр важен
    registration_page.check_hobbies('y', 'n', 'y') # 'y' или 'n' по желаемому хобби
    registration_page.add_file("../tests/Octopus.jpg")
    registration_page.fill_adress('Moscow, Bulkina 65-39')
    registration_page.choose_state('Haryana')
    registration_page.choose_city('Panipat')
    registration_page.submit()

    # Проверки
    Assert_results.in_submit_form()