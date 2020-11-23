from django.conf import settings
from oauth2_provider.models import Application, AccessToken, RefreshToken
from core.auth.utils import random_token_generator
import os, datetime

class Token(object):

    @classmethod
    def get_client_application(cls, client_id, client_secret):
        try:
            return Application.objects.get(client_id=client_id, client_secret=client_secret)
        except:
            return None

    @classmethod
    def create_token_response(cls, user, data):
        if user is None:
            return False, "User not found"
            
        token = random_token_generator()
        expire_seconds = settings.OAUTH2_PROVIDER["ACCESS_TOKEN_EXPIRE_SECONDS"]
        scopes = settings.OAUTH2_PROVIDER['SCOPES']

        application = None
        application = cls.get_client_application(data["client_id"], data["client_secret"])

        if application is None:
            return False, "Invalid client id & client secret"
        
        expires = datetime.datetime.now() + datetime.timedelta(seconds=expire_seconds)

        access_token = AccessToken.objects.create(user=user, application=application, token=token, expires=expires,scope=scopes)


        refresh_token = RefreshToken.objects.create(user=user,token=token,access_token=access_token,application=application)

        return True, {
            'access_token': access_token.token,
            'token_type': 'Bearer',
            'expires_in': expire_seconds,
            'refresh_token': refresh_token.token,
            'scope': scopes
        }
