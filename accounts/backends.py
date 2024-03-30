from typing import Any
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth import get_user_model

# This backend is not beign user!!!
class EmailBackend(ModelBackend):
    def authenticate(self, request, username, password, **kwargs):
        if username is None or password is None:
            return None

        USER_MODEL = get_user_model()

        try:
            user = USER_MODEL.objects.get(email=username)
        except USER_MODEL.DoesNotExist:
            return None

        if user.check_password(password):
            return user

        return None


