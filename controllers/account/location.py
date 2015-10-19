from google.appengine.ext import ndb
from models.Location import Location
from controllers.account.account_base import AccountBaseHandler
from models.Company import Company


class LocationHandler(AccountBaseHandler):

    @ndb.toplevel
    def get(self, location_id):
        location = Location.get_by_id(int(location_id))
        self.template_values['location'] = location
        self.response.out.write("boop")
    
    @ndb.toplevel
    def post(self):
        company_id = int(self.request.get('company-id'))
        location_kwargs = {
            'company': Company.get_by_id(company_id),
            'name': self.request.get('name'),
            'country': self.request.get('country'),
            'state': self.request.get('state'),
            'city': self.request.get('city'),
            'location_type': self.request.get('location-type'),
            'adult_ads_restricted': bool(int(self.request.get('adult-ads-restricted'))),
            'adult_oriented': bool(int(self.request.get('adult-oriented')))
        }
        new_location = Location.create_location(**location_kwargs)

class LocationCreateHandler(AccountBaseHandler):

    @ndb.toplevel
    def get(self):
        self.render_template('account/location/location_new_edit.html')