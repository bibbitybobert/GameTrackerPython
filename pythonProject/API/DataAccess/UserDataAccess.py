from sys import exception

from API.Services.databaseContext import *
from API.Models.User import User
from API.Models.Session import Session as UserSession

class UserDataAccess:
    def get_user_by_id(self, user_id):
        session = Session()
        try:
            user = session.query(User).filter(User.id == user_id).first()
            return user
        except Exception as e:
            print(e)
            return None
        finally:
            session.close()

    def get_all_users(self):
        session = Session()
        try:
            users = session.query(User).all()
            return users
        except Exception as e:
            print(e)
            return None
        finally:
            session.close()

    def get_user_by_email(self, email):
        session = Session()
        try:
            user = session.query(User).filter(User.email == email).first()
            return user
        except Exception as e:
            print(e)
            return None
        finally:
            session.close()

    def create_session(self, user: User):
        session = Session()
        try:
            new_session = UserSession(user.id)
            session.add(new_session)
            session.commit()
            return new_session.id, new_session.expiresAt
        except Exception as e:
            print(e)
            return None, None
        finally:
            session.close()

    def add_new_user(self, fName, lName, email, passwordHash):
        session = Session()
        try:
            new_user = User(fName, lName, email, passwordHash)
            session.add(new_user)
            session.commit()
            return session.query(User).filter(User.id == new_user.id).first()
        except Exception as e:
            print(e)
            return False
        finally:
            session.close()

    def get_session_by_token(self, session_token):
        session = Session()
        try:
            out_session = session.query(UserSession).filter(UserSession.id == session_token).first()
            return out_session
        except Exception as e:
            print(e)
            return None
        finally:
            session.close()

    def remove_session_by_token(self, session_token):
        session = Session()
        try:
            sessionRes = session.query(UserSession).filter(UserSession.id == session_token).first()
            if sessionRes is None:
                raise Exception("session not found")

            session.delete(sessionRes)
            session.commit()
            return True
        except Exception as e:
            print(e)
            return False
        finally: session.close()

    def renew_session_by_token(self, session_token):
        session = Session()
        try:
            sessionRes = session.query(UserSession).filter(UserSession.id == session_token).first()
            if sessionRes is None:
                raise Exception("session not found")

            (session.query(UserSession).filter(UserSession.id == session_token)
                   .update({'expiresAt': sessionRes.renew_time()}))
            session.commit()
            return session.query(UserSession).filter(UserSession.id == session_token).first()
        except Exception as e:
            print(e)
            return None
        finally:
            session.close()

