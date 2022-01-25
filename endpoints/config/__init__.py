import os


if os.environ.get('FLASK_ENV') == 'production':
    from endpoints.config.production import *
elif os.environ.get('FLASK_ENV') == 'staging':
    from endpoints.config.staging import *
else:
    from endpoints.config.develop import *
