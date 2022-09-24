import jwt
from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Depends,
    Header,
    Cookie,
    HTTPException,
)
from uuid import uuid4
from typing import (
    Union,
    List,
)
from fastapi.responses import JSONResponse, FileResponse

from app.settings import (
    VERIFICATION_COOKIE_NAME,
    MEDIA_DIR_PATH,
)
from app.utils import (
    make_path_for_media
)
from app.security.model import VerificationToken
from app.security.exceptions import (
    BaseSecurityException
)
from app.editor.model import (
    VideoSchema,
    get_video_ids_from_schema
)
from app.editor.editor import Editor


router = APIRouter()


@router.post("/process", response_class=FileResponse)
def process(video_schema: VideoSchema, token: Union[str, None] = Cookie(default=None, alias=VERIFICATION_COOKIE_NAME)):
    try:
        VerificationToken.check_uids_validity(get_video_ids_from_schema(video_schema), token)
    except BaseSecurityException as e:
        raise HTTPException(status_code=400, detail=str(e))

    # TODO maybe some logic for validation options

    editor = Editor(MEDIA_DIR_PATH)
    return editor.process(video_schema)
