from werkzeug.security import safe_str_cmp
from models.user import UserModel


def authenticate(username, password):
    """
    Function  that gets called when a user calls the /auth endpoint
    with their username and password.
    :param username: User's username in string format.
    :param password: User's un-encryptet password in string format.
    :return: A UseerModel object if authentication was successful, None otherwise.
    """

    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        user
    return None


def identify(payload):
    """
    Function that gets called when user has already authenticated and Flask-JWT
    verified their authorization header is correct.
    :param payload: A dictionary with 'identity key, which is the user id.
    :return: A UserModel object.
    """

    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
