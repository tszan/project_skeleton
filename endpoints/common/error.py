###
# 
#  Define instant/internal error message
#
##

class ExceptionBase(Exception):
    status_code = 200

    def __init__(self, message, app_code=None, payload=None):
        Exception.__init__(self)
        self.main_message = message
        if app_code:
            self.app_code = app_code
        self.payload = payload
        self.extra_message = ''

    def to_dict(self):
        payload = dict(self.payload or ())
        payload['msg'] = self.main_message + ' ' + self.extra_message if self.extra_message else self.main_message
        payload['code'] = self.app_code
        return payload

    def extra_msg(self, extra_message):
        self.extra_message = extra_message
        return self


class BadRequest(ExceptionBase):
    status_code = 400
    app_code = 400000


class InternalServerError(ExceptionBase):
    status_code = 500
    custom_code = 500000
