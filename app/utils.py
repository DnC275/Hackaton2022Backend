import jwt
from pathlib import Path
import logging
import sys

from app.settings import (
    MEDIA_DIR_PATH,
)


def make_path_for_media(filename: str):
    return MEDIA_DIR_PATH / filename

def create_logger():
    root = logging.getLogger()
    root.setLevel(logging.INFO)

    handler = logging.StreamHandler(sys.stderr)
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    root.addHandler(handler)
