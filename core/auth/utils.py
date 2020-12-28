import uuid
import secrets

'''
The secrets module is part of the Python standard library in Python 3.6 and newer
'''

def random_token_generator():
    return secrets.token_urlsafe(20)