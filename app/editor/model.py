import dataclasses
import typing


@dataclasses.dataclass
class Fragment:
    video_id: str
    begin: int # frame number
    end: int # frame number


@dataclasses.dataclass
class VideoSchema:
    fragments: typing.List[Fragment]
    format: str # .avi, .mkv, .mp4

    
