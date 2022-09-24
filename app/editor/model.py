import dataclasses
import typing


@dataclasses.dataclass
class Fragment:
    video_id: str
    begin: int  # second
    end: int  # second


@dataclasses.dataclass
class VideoSchema:
    fragments: typing.List[Fragment]
    format: str  # .avi, .mkv, .mp4


def get_video_ids_from_schema(schema: VideoSchema):
    ids_set = set()
    for fragment in schema.fragments:
        ids_set.add(fragment.video_id)

    return ids_set

    
