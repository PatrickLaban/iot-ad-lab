from google.appengine.ext import ndb
from ModelBase import ModelBase


class Asset(ModelBase):
    asset_data = ndb.BlobProperty()

    @classmethod
    def create_asset(cls, asset_data):
        new_asset = Asset(asset_data=asset_data)
        new_asset.put()
        return new_asset
