import datetime
import random
import string


class Session:
    def __init__(self, user_info):
        self.__session_id = self.get_random_string(16)
        self.__user_info = user_info
        self.__time_exp = self.time_expiration()

    @property
    def session_id(self):
        return self.__session_id

    @property
    def time_exp(self):
        return self.__time_exp

    def session_obj(self):
        return {
            self.__session_id: {
                "time_exp": str(self.__time_exp),
                "user_info": self.__user_info,
            }
        }

    def time_expiration(self, hours=1):
        current_date_time = datetime.datetime.utcnow()
        future_date_time = current_date_time + datetime.timedelta(hours=hours)
        return future_date_time.strftime("%a, %d %b %Y %H:%M:%S GMT")

    @staticmethod
    def get_random_string(length):
        # choose from all lowercase letter
        letters = string.ascii_lowercase
        result_str = "".join(random.choice(letters) for i in range(length))
        return result_str
