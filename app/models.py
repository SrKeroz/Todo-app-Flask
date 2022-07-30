from flask_login import UserMixin
from .firestore_service import get_user_id


class UserData:
    def __init__(self, username, password):
        self.username = username
        self.password = password


class UserModel(UserMixin):
    def __init__(self, user_data):
        """
        :Param user_data: UserData
        """
        self.id = user_data.username
        self.password = user_data.password

    
    @staticmethod
    def query(user_id):
        user_doc = get_user_id(user_id)
        user_data = UserData(user_id = user_doc.id, password= user_doc.to_dict()["password"])

        return UserModel(user_data)