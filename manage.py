from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from endpoints import APP, DB


migrate = Migrate(APP, DB)

manager = Manager(APP)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
