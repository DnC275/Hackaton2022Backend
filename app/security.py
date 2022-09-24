import json
import jwt
from typing import (
    List,
    Optional,
)

from app.settings import SECRET_FOR_JWT


class VerificationToken:
    def __init__(self, uids: Optional[List[str]]):
        if not isinstance(uids, list):
            uids = [uids]
        self.media_uids = uids

    @staticmethod
    def create_token(filename, encoded_token=None):
        if encoded_token:
            decoded_token = jwt.decode(encoded_token, SECRET_FOR_JWT, algorithms='HS256')
            token_data = json.loads(decoded_token)
            token = VerificationToken(token_data['media_uids'] + [filename])
        else:
            token = VerificationToken(filename)

        return jwt.encode(vars(token), SECRET_FOR_JWT, algorithm='HS256')

