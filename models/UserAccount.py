from google.appengine.ext import ndb
from google.appengine.api import users

from ModelBase import ModelBase

ACCOUNT_TYPE = {"Normal": 1, "UnitManager": 2}
ACCOUNT_STATE = {"Active": 1, "Banned": -1} #TODO: Account deletion

class AccountTypes(object):
    NORMAL = 1
    UNIT_MANAGER = 2

class AccountStates(object):
    ACTIVE = 1
    BANNED = -1


class UserAccount(ModelBase):
    google_id = ndb.StringProperty()
    email = ndb.StringProperty()
    name = ndb.StringProperty()
    type = ndb.IntegerProperty(choices=[AccountTypes.NORMAL, AccountTypes.UNIT_MANAGER], default=AccountTypes.NORMAL)
    state = ndb.IntegerProperty(choices=[AccountStates.ACTIVE, AccountStates.BANNED], default=AccountStates.ACTIVE)

    @classmethod
    def get_user_account(cls):
        google_user = users.get_current_user()
        if google_user is None:
            return None
        # TODO: Memcache lookup user by google id
        user_account_query = cls.query(cls.google_id == google_user.user_id()).fetch()
        if user_account_query:
            user_account = user_account_query[0]
        else:
            user_account = UserAccount(google_id=google_user.user_id(),
                                       email=google_user.email(),
                                       name=google_user.nickname())
            user_account.put()
        return user_account


