import jwt

from typing import (
    List,
    Optional,
)
from app.settings import SECRET_FOR_JWT
from app.security.utils import decode_jwt
from app.security.exceptions import (
    UidsDoesntMatchTokenException,
)


class VerificationToken:
    def __init__(self, uids: Optional[List[str]]):
        if uids is None:
            uids = []
        elif not isinstance(uids, list):
            uids = [uids]
        self.media_uids = uids

    # TODO annotations
    # создает новый зашифрованный токен на основе файла и старого токена(если он был)
    @classmethod
    def create_token(cls, filename, token=None):
        validation_token = get_token(token)
        validation_token.media_uids.append(filename)
        return jwt.encode(vars(validation_token), SECRET_FOR_JWT, algorithm='HS256')

    @classmethod
    def check_uids_validity(cls, uids, token):
        validation_token = get_token(token)
        if any(uid not in validation_token.media_uids for uid in uids):
            raise UidsDoesntMatchTokenException()


def get_token(token=None) -> 'VerificationToken':
    if token is None:
        return VerificationToken([])
    if isinstance(token, VerificationToken):
        return token

    decoded_token = decode_jwt(token)
    token = VerificationToken(decoded_token['media_uids'])
    return token
