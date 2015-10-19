import json

from google.appengine.ext import ndb
from controllers.account.account_base import AccountBaseHandler
from models.Asset import Asset


class AssetHandler(AccountBaseHandler):

    @ndb.toplevel
    def get(self, asset_id):
        asset = Asset.get_by_id(int(asset_id))
        self.response.headers['Content-Type'] = 'image/jpeg'
        self.response.write(asset.asset_data)

    @ndb.toplevel
    def post(self):
        asset_data = str(self.request.get('asset-data'))
        new_asset = Asset.create_asset(asset_data=asset_data)
        response = {'success': True, 'goto_url': '/account/'}
        self.response.write(json.dumps(response))

    """
    @ndb.toplevel
    def put(self, company_id):
        company = Company.get_by_id(int(company_id))
        name = self.request.get('name')
        if Company.query(Company.name == name).count() > 0:
            response = {'success': False, 'error_message': "A company already exists with the name {0}".format(name)}
            self.response.write(json.dumps(response))
            return
        company.edit_company(name=name)
        response = {'success': True, 'goto_url': '/account/company/{0}'.format(company.key.id())}
        self.response.write(json.dumps(response))
    """

class AssetCreateHandler(AccountBaseHandler):
    @ndb.toplevel
    def get(self):
        self.render_template('account/asset/asset_new_edit.html')

"""
class CompanyEditHandler(AccountBaseHandler):
    @ndb.toplevel
    def get(self, company_id):
        company = Company.get_by_id(int(company_id))
        self.template_values['company'] = company
        self.render_template('account/company/company_new_edit.html')
"""