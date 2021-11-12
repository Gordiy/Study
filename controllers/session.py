import random
import string


class Session:
    def __init__(self, data):
        self.__session_id = self.get_random_string(16)
        self.__data = data

    def session_obj(self):
        return {
            self.__session_id: {
                "data": self.__data
            }
        }

    @property
    def session_id(self):
        return self.__session_id

    @staticmethod
    def get_random_string(length):
        # choose from all lowercase letter
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str
    