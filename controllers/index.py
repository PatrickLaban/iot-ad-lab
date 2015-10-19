from handler_base import BaseHandler
from google.appengine.ext import ndb


class IndexHandler(BaseHandler):

    @ndb.toplevel
    def get(self):
        self.render_template('index.html')