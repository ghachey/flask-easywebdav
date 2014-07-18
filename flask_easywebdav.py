import easywebdav
from flask import current_app

# Find the stack on which we want to store the database connection.
# Starting with Flask 0.9, the _app_ctx_stack is the correct one,
# before that we need to use the _request_ctx_stack.
try:
    from flask import _app_ctx_stack as stack
except ImportError:
    from flask import _request_ctx_stack as stack


class EasyWebDAV(object):

    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    # Not using this yet
    # def init_app(self, app):
    #     # No default connection for easywebdav
    #     # app.config.setdefault('SQLITE3_DATABASE', ':memory:')
    #     # Use the newstyle teardown_appcontext if it's available,
    #     # otherwise fall back to the request context
    #     if hasattr(app, 'teardown_appcontext'):
    #         app.teardown_appcontext(self.teardown)
    #     else:
    #         app.teardown_request(self.teardown)

    def connect(self):
        webdav_conf = current_app.config['WEBDAV_SERVER']
        # TODO: Check config
        webdav = webdav.connect(host, 
                                username=webdav_conf['username'], 
                                password=webdav_conf['password'],
                                protocol=webdav_conf['protocol'], 
                                port=webdav_conf['port'], 
                                verify_ssl=webdav_conf['verify_ssl'])
        return webdav

    def teardown(self, exception):
        ctx = stack.top
        if hasattr(ctx, 'sqlite3_db'):
            ctx.sqlite3_db.close()

    @property
    def connection(self):
        ctx = stack.top
        if ctx is not None:
            if not hasattr(ctx, 'webdav_endpoint'):
                ctx.webdav_endpoint = self.connect()
            return ctx.webdav_endpoint
