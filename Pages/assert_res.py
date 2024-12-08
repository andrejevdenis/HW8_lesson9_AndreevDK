from selene import browser, have, be

class Assert_results:

    @classmethod
    def in_submit_form(cls):
        browser.element('[class="modal-header"]').should(have.text('Thanks for submitting the form'))
        browser.element('[class="table-responsive"]').should(have.text('Fedor Lomovoy'))
        browser.element('[class="table-responsive"]').should(have.text('fedyaosminog@ramb.com'))
        browser.element('[class="table-responsive"]').should(have.text('Other'))
        browser.element('[class="table-responsive"]').should(have.text('1000000000'))
        browser.element('[class="table-responsive"]').should(have.text('23 October,2000'))
        browser.element('[class="table-responsive"]').should(have.text('Maths, Computer Science'))
        browser.element('[class="table-responsive"]').should(have.text('Sports, Music'))
        browser.element('[class="table-responsive"]').should(have.text('Octopus.jpg'))
        browser.element('[class="table-responsive"]').should(have.text('Moscow, Bulkina 65-39'))
        browser.element('[class="table-responsive"]').should(have.text('Haryana Panipat'))