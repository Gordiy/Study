from .session import Session

class User:
    def __init__(self, username, password):
        self.__user_id = Session.get_random_string(8)
        self.__username = username
        self.__password = password
        self.__isActive = False
    
    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__password

    @property
    def active(self):
        return self.__isActive

    def get_user(self):
        return {
            self.__user_id: {
                'username': self.__username,
                'password': self.__password,
                'is_active': self.__isActive,
            }
        }

    def activate(self):
        self.__isActive = True

    def deactivate(self):
        self.__isActive = False
