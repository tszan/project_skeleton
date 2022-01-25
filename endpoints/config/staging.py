
DEBUG = False
TESTING = False
BUNDLE_ERRORS = True
SECRET_KEY = 'e2e65f8560a1573549aa187d56325a8e153452fd94dcdaacf0ee26e1e11e4eba'

## Replace to real db uri ##
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://test:password@localdb/db'

SQLALCHEMY_TRACK_MODIFICATIONS = False