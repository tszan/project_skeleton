from endpoints import DB


## Create Database Model
class User(DB.Model):
    __tablename__ = 'user'

    id = DB.Column(DB.Integer, primary_key=True, nullable=False)
    name = DB.Column(DB.String(20))
    email = DB.Column(DB.String(50))

    def __repr__(self):
        return 'Id: {}, name: {}, email: {}'.format(self.id, self.name, self.email)
