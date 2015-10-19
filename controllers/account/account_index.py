from google.appengine.ext import ndb
from models.CompanyAccount import CompanyAccount
from controllers.account.account_base import AccountBaseHandler


class IndexBaseHandler(AccountBaseHandler):

    @ndb.toplevel
    def get(self):
        company_account_query = CompanyAccount.query(CompanyAccount.user_account_key == self.user_account.key)
        companies = [company_account.company for company_account in company_account_query]
        self.template_values['user_companies'] = companies
        self.render_template('account/index.html')