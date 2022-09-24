import os
import typing

def get_env(env, default: typing.Optional[str] = None):
    return os.environ.get(env, default)

VERIFICATION_COOKIE_NAME = 'token'
MEDIA_DIR_PATH = get_env('MEDIA_PATH', './data')
SECRET_FOR_JWT = get_env('JWT_SECRET', 'secret')
