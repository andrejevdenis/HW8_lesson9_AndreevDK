import os.path
from selene import browser, have, be

from selenium.webdriver import Keys

class RegistrationPage:

    @classmethod
    def fill_first_name(cls, value):
       browser.element('[id="firstName"]').type(value)

    @classmethod
    def fill_last_name(cls, value):
        browser.element('[id="lastName"]').type(value)

    @classmethod
    def fill_email(cls, value):
        browser.element('[id="userEmail"]').type(value)

    @classmethod
    def fill_gender(cls, value):
        if value == 'Male':
            browser.element('[for="gender-radio-1"]').click()  # Male
        elif value == 'Female':
            browser.element('[for="gender-radio-2"]').click()  # Male
        else:
            browser.element('[for="gender-radio-3"]').click()  # Male

    @classmethod
    def fill_mobile_num(cls, param):
        browser.element('[id="userNumber"]').type(param).press_tab()

    @classmethod
    def fill_date_of_birth(cls, month, year, day):
        browser.element('[class="react-datepicker__month-select"]').element(f'[value="{month}"').click()
        browser.element('[class="react-datepicker__year-select"]').element(f'[value="{year}"]').click()
        browser.element(f'[class="react-datepicker__day react-datepicker__day--0{day}"]').click()

    @classmethod
    def add_subject(self, param):
        browser.element('[id="subjectsInput"]').type(param)
        browser.element('[id="react-select-2-option-0"]').click()
        return self


    @classmethod
    def check_hobbies(cls, Sports, Reading, Music):
        if Sports == 'y':
            browser.element('[for="hobbies-checkbox-1"]').click()
        if Reading == 'y':
            browser.element('[for="hobbies-checkbox-2"]').click()
        if Music == 'y':
            browser.element('[for="hobbies-checkbox-3"]').click()

    @classmethod
    def add_file(cls, param):
        browser.element('[id="uploadPicture"]').set_value(os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), f'resources/{param}')))

    @classmethod
    def fill_adress(cls, param):
        browser.element('[id="currentAddress"]').type(param).press_tab().press(Keys.PAGE_DOWN)

    @classmethod
    def choose_state(cls, param):
        browser.element('[id="state"]').click()
        if param == 'NCR':
            browser.element('[id="react-select-3-option-0"]').click()
        elif param == 'Uttar Pradesh':
            browser.element('[id="react-select-3-option-1"]').click()
        elif param == 'Haryana':
            browser.element('[id="react-select-3-option-2"]').click()
        elif param == 'Rajasthan':
            browser.element('[id="react-select-3-option-3"]').click()

    @classmethod
    def choose_city(cls, param):
        browser.element('[id="city"]').click()
        if param in ['Delhi', 'Agra', 'Karnal', 'Jaipur']:
            browser.element('[id="react-select-4-option-0"]').click()
        elif param in ['Gurgaon', 'Lucknow', 'Panipat', 'Jaiselmer']:
            browser.element('[id="react-select-4-option-1"]').click()
        elif param in ['Noida', 'Merrut']:
            browser.element('[id="react-select-4-option-2"]').click()

    @classmethod
    def submit(cls):
        browser.element('[id="submit"]').click()