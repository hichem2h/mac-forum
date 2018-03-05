from app.models import User
from app import db


class UserRepository:

    def __init__(self, session):
        self.session = session()

    def add(self, entity):
        try:
            self.session.add(entity)
            self.session.commit()
        except:
            self.session.rollback()
            raise
        finally:
            self.session.close()


class UserEditor:

    @staticmethod
    def register_user(username, birth_date, password):
        user = User(username=username, birth_date=birth_date)
        user.set_password(password)

        try:
            UserRepository(db.session).add(user)
        except:
            return 'There was an error, please try again'