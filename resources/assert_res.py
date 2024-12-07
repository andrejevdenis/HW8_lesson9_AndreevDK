from selene import browser, have, be

class Assert_results:

    @classmethod
    def shuld_have_thanks(cls, param):
        browser.element('[class="modal-header"]').should(have.text(param))

    @classmethod
    def shuld_have_fname_lname(cls, param):
        browser.element('[class="table-responsive"]').should(have.text(param))

    @classmethod
    def shuld_have_email(cls, param):
        browser.element('[class="table-responsive"]').should(have.text(param))

    @classmethod
    def shuld_have_gender(cls, param):
        browser.element('[class="table-responsive"]').should(have.text(param))

    @classmethod
    def shuld_have_mobile_num(cls, param):
        browser.element('[class="table-responsive"]').should(have.text(param))

    @classmethod
    def shuld_have_birth_date(cls, param):
        browser.element('[class="table-responsive"]').should(have.text(param))

    @classmethod
    def shuld_have_subject(self, param):
        browser.element('[class="table-responsive"]').should(have.text(param))

    @classmethod
    def shuld_have_hobbies(self, param):
        browser.element('[class="table-responsive"]').should(have.text(param))

    @classmethod
    def file_name(cls, param):
        browser.element('[class="table-responsive"]').should(have.text(param))

    @classmethod
    def adress(cls, param):
        browser.element('[class="table-responsive"]').should(have.text(param))

    @classmethod
    def sname_cname(cls, param):
        browser.element('[class="table-responsive"]').should(have.text(param))

