import json
import logging

from django.forms import model_to_dict

from .models import User
from .utils import get_response

logging.basicConfig(filename='file.log', filemode='w', level=logging.DEBUG)


def register_user(request):
    """Function to register user details"""
    try:
        data = json.loads(request.body)
        if request.method == 'POST':
            user = User.objects.create(username=data.get('username'), password=data.get('password'),
                                       first_name=data.get('first_name'), last_name=data.get('last_name'),
                                       email=data.get('email'), phone_no=data.get('phone_no'))
            return get_response(data=model_to_dict(user, exclude=("password",)), status=201)
        return get_response(status=405)

    except Exception as e:
        logging.exception(e)
        return get_response(message=str(e), status=400)


def login_user(request):
    """Function to login the user"""
    try:
        data = json.loads(request.body)
        if request.method == "POST":
            user = User.objects.filter(username=data.get('username'), password=data.get('password')).first()
            if user is not None:
                return get_response(data=model_to_dict(user, exclude=("password",)), message="login successful",
                                    status=200)
            return get_response(status=406)
        return get_response(status=405)

    except Exception as e:
        logging.exception(e)
        return get_response(message=str(e), status=400)
    