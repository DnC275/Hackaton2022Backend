import jwt
from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Cookie,
    HTTPException,
)
from uuid import uuid4
from typing import (
    Union,
    Optional,
    List,
)
from fastapi.responses import JSONResponse

from app.settings import VERIFICATION_COOKIE_NAME
from app.utils import (
    make_path_for_media
)
from app.security import VerificationToken


router = APIRouter()


@router.post("/upload")
def upload(file: UploadFile = File(...), token: Optional[str] = Cookie(default=None, alias=VERIFICATION_COOKIE_NAME)):
    try:
        media_uid = uuid4().hex
        path = make_path_for_media(media_uid)
        with open(path, 'wb') as f:
            f.write(file.file.read())
    except OSError:
        raise HTTPException(status_code=400, detail="Failed to load media")
    finally:
        file.file.close()

    token = VerificationToken.create_token(media_uid, token=token)

    response = JSONResponse(media_uid)
    response.set_cookie(key=VERIFICATION_COOKIE_NAME, value=token)
    return response


@router.get("/ping")
def ping(cookie: Union[str, None] = Cookie(default=None, alias='token')):
    print(cookie)
    return {"message": "ok"}
