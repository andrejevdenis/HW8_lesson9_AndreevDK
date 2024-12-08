from selene import browser, have, be

class Assert_results:

    @classmethod
    def in_submit_form(cls, value):
        browser.element('[class="modal-header"]').should(have.text('Thanks for submitting the form'))
        browser.element('[class="table-responsive"]').should(have.text(f'{value.first_name} {value.last_name}'))
        browser.element('[class="table-responsive"]').should(have.text(value.email))
        browser.element('[class="table-responsive"]').should(have.text(value.gender))
        browser.element('[class="table-responsive"]').should(have.text(value.mobile_num))
        browser.element('[class="table-responsive"]').should(have.text(f'{value.date_of_birth.get('day')} {value.date_of_birth.get('month')},{value.date_of_birth.get('year')}'))
        browser.element('[class="table-responsive"]').should(have.text(f'{value.subject}, {value.subject1}'))
        if value.hobbies.get('Sports') == 'y':
            browser.element('[class="table-responsive"]').should(have.text('Sports'))
        if value.hobbies.get('Reading') == 'y':
            browser.element('[class="table-responsive"]').should(have.text('Reading'))
        if value.hobbies.get('Music') == 'y':
            browser.element('[class="table-responsive"]').should(have.text('Music'))
        browser.element('[class="table-responsive"]').should(have.text(value.file))
        browser.element('[class="table-responsive"]').should(have.text(value.adress))
        browser.element('[class="table-responsive"]').should(have.text(f'{value.state} {value.city}'))