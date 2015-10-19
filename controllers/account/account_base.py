from controllers.handler_base import BaseHandler


class AccountBaseHandler(BaseHandler):

    def __init__(self, request, response):
        super(AccountBaseHandler, self).__init__(request, response)