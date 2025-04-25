from API.DataAccess.UserDataAccess import UserDataAccess
import hashlib

class UsersUseCase:
    def __init__(self):
        self._dataAccess = UserDataAccess()

    def get_user_by_id(self, user_id):
        return self._dataAccess.get_user_by_id(user_id)

    def get_user_by_email(self, email):
        user = self._dataAccess.get_user_by_email(email)
        if user is not None:
            return True, user
        return False, None

    def get_all_users(self):
        return self._dataAccess.get_all_users()

    def login(self, email, password):
        user = self._dataAccess.get_user_by_email(email)
        if user is None:
            return False, {"error", "User not found"}

        hashed_pass = hashlib.sha256(password.encode()).hexdigest()
        if user.passwordHash != hashed_pass:
            return False, {"error", "Incorrect Password"}

        return True, user

    def register(self, firstName, lastName, email, password):
        existing_user = self._dataAccess.get_user_by_email(email)
        if existing_user is not None:
            return False, {"error", "User already exists"}

        new_user = self._dataAccess.add_new_user(firstName, lastName, email, hashlib.sha256(password.encode()).hexdigest())
        return self.login(new_user.email, password)

    def validate_session_token(self, session_token):
        session = self._dataAccess.get_session_by_token(session_token)
        user = self._dataAccess.get_user_by_id(session.user_id)
        if session is None:
            return False, {"error", "Session not found"}
        if user is None:
            return False, {"error", "User not found"}
        return True, {session, user}

    def remove_session(self, session_token):
        result = self._dataAccess.remove_session_by_token(session_token)
        if not result:
            return False, {"error", "Unable to remove session"}
        return True, {"success": True}

    def renew_session(self, session_token):
        result = self._dataAccess.renew_session_by_token(session_token)
        if result is None:
            return False, {"error", "Unable to renew session"}
        return True, result


