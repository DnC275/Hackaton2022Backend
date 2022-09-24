import json
import jwt
from typing import (
    List,
    Optional,
)
from fastapi import Depends

from app.settings import SECRET_FOR_JWT


class VerificationToken:
    def __init__(self, uids: Optional[List[str]]):
        if uids is None:
            uids = []
        elif not isinstance(uids, list):
            uids = [uids]
        self.media_uids = uids

    # создает новый зашифрованный токен на основе файла и старого токена(если он был)
    @classmethod
    def create_token(cls, filename, token=None):
        validation_token = get_token(token)
        validation_token.media_uids.append(filename)
        return jwt.encode(vars(validation_token), SECRET_FOR_JWT, algorithm='HS256')

    # @staticmethod
    # def check_uids_validity(uids, token = Depends(get_token)):
    #     for uid in uids:


def get_token(token=None) -> VerificationToken:
    if token is None:
        return VerificationToken([])
    if isinstance(token, VerificationToken):
        return token

    decoded_token = decode_jwt(token)
    token = VerificationToken(decoded_token['media_uids'])
    return token


def decode_jwt(encoded_token):
    return jwt.decode(encoded_token, SECRET_FOR_JWT, algorithms='HS256')