import webapp2
import controllers.account.company
import controllers.account.account_index
import controllers.account.asset
import controllers.account.location

app = webapp2.WSGIApplication(
    [('/account/company_create/?', controllers.account.company.CompanyCreateHandler),
     ('/account/company_edit/(\d+)', controllers.account.company.CompanyEditHandler),
     ('/account/company/(\d+)', controllers.account.company.CompanyHandler),
     ('/account/company/?', controllers.account.company.CompanyHandler),
     ('/account/asset_create/?', controllers.account.asset.AssetCreateHandler),
     ('/account/asset/(\d+)', controllers.account.asset.AssetHandler),
     ('/account/asset/?', controllers.account.asset.AssetHandler),
     ('/account/location_create/?', controllers.account.location.LocationCreateHandler),
     ('/account/location/(\d+)', controllers.account.location.LocationHandler),
     ('/account/location/?', controllers.account.location.LocationHandler),
     ('/account/?', controllers.account.account_index.IndexBaseHandler),
    ], debug=True)
