# flask packages
from flask_restful import Api

# project resources
from .authentication import SignUpApi, LoginApi
from .user import UsersApi, UserApi
from .meal import MealsApi, MealApi


def create_routes(api: Api):
    """Adds resources to the api.
    :param api: Flask-RESTful Api Object

    """
    api.add_resource(SignUpApi, '/authentication/signup/')
    api.add_resource(LoginApi, '/authentication/login/')

    api.add_resource(UsersApi, '/user/')
    api.add_resource(UserApi, '/user/<user_id>')

    api.add_resource(MealsApi, '/meal/')
    api.add_resource(MealApi, '/meal/<meal_id>')
