from google.appengine.ext import ndb
from ModelBase import ModelBase


class Location(ModelBase):
    name = ndb.StringProperty(required=True)
    country = ndb.StringProperty()
    state = ndb.StringProperty()
    city = ndb.StringProperty()
    location_type = ndb.StringProperty()
    adult_ads_restricted = ndb.BooleanProperty()
    adult_oriented = ndb.BooleanProperty()
    company_key = ndb.KeyProperty(kind='Company')

    def __init__(self, *args, **kwargs):
        super(Location, self).__init__(*args, **kwargs)
        self._company = None

    @property
    def company(self):
        if self._company is None:
            self._company = Company.get_by_id(self.company_key.id())
        return self._company

    @classmethod
    def create_location(cls, **kwargs):
        new_location = Location(
            name=kwargs['name'],
            country=kwargs['country'],
            state=kwargs['state'],
            city=kwargs['city'],
            location_type=kwargs['location_type'],
            adult_ads_restricted=kwargs['adult_ads_restricted'],
            adult_oriented=kwargs['adult_oriented'],
            company_key=kwargs['company'].key,
        )
        new_location.put()
        return new_location
    #
    #
    # def edit_company(self, name):
    #     self.name = name
    #     self.put()