import jwt
from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Depends,
    Header,
    Cookie,
)
from uuid import uuid4
from typing import (
    Union,
    List,
)
from fastapi.responses import JSONResponse

# from ..main import (
#     VERIFICATION_COOKIE_NAME,
# )

from app.settings import VERIFICATION_COOKIE_NAME
from app.utils import (
    make_path_for_media
)
from app.security import VerificationToken


router = APIRouter()


@router.post("/upload")
def upload(file: UploadFile = File(...), token: Union[str, None] = Cookie(default=None, alias=VERIFICATION_COOKIE_NAME)):
    try:
        media_uid = uuid4().hex
        path = make_path_for_media(media_uid)
        print(path)
        with open(path, 'wb') as f:
            f.write(file.file.read())
    except OSError:
        return JSONResponse('failed', status_code=400)
    finally:
        file.file.close()

    token = VerificationToken.create_token(media_uid, token)

    response = JSONResponse(media_uid)
    response.set_cookie(key=VERIFICATION_COOKIE_NAME, value=token)
    return response


@router.get("/ping")
def ping(cookie: Union[str, None] = Cookie(default=None, alias='token')):
    print(cookie)
    return {"message": "OK"}
