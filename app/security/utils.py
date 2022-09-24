import jwt

from app.settings import (
    SECRET_FOR_JWT
)


def decode_jwt(encoded_token):
    return jwt.decode(encoded_token, SECRET_FOR_JWT, algorithms='HS256')