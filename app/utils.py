import jwt
from pathlib import Path

from app.settings import (
    MEDIA_DIR_PATH,
)


def make_path_for_media(filename: str):
    return MEDIA_DIR_PATH / filename
