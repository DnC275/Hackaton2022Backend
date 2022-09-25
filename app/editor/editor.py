import ffmpeg
import pathlib
import uuid
import logging

import subprocess

import app.editor.model as model
from app.utils import create_logger

create_logger()

logger = logging.getLogger('editor')

class Editor:
    def __init__(self, data_path: pathlib.Path):

        self._data_path = data_path
        self._out_base_path = data_path / "out"

        if not self._out_base_path.exists():
            self._out_base_path.mkdir()

    def process(self, video_schema: model.VideoSchema) -> pathlib.Path:

        self._cached_inputs = []

        trimed_inputs = [
            self._trim(self._data_path / fragment.video_id, fragment.begin, fragment.end)
            for fragment in video_schema.fragments
        ]

        concated_fragments = ffmpeg.concat(*sum(trimed_inputs, ()), v=1, a=1)

        # TODO: Text, images

        out_id = uuid.uuid4()
        out_path = self._out_base_path / f"{out_id.hex}{video_schema.format}"

        concated_fragments.output(str(out_path)).run()

        self._cached_inputs = None

        return out_path

    def _trim(self, path, start, end):
        assert self._cached_inputs is not None

        input_audio = ffmpeg.probe(path, select_streams='a')
        has_no_audio = not input_audio["streams"]

        input = ffmpeg.input(path)
        vid = input.video.trim(start=start, end=end).setpts("PTS-STARTPTS")

        self._cached_inputs.append(input)

        if not has_no_audio:
            aud = input.audio.filter("atrim", start=start, end=end).filter(
                "asetpts", "PTS-STARTPTS"
            )

            return (vid, aud)
        else:
            logger.info('Creating silent audio')
            
            audio_filename = self._out_base_path / f'{uuid.uuid4().hex}.ac3'
            process = subprocess.Popen(
                [
                    "ffmpeg",
                    "-f",
                    "lavfi",
                    "-i",
                    "anullsrc=channel_layout=5.1:sample_rate=48000",
                    "-t",
                    str(end - start),
                    str(audio_filename),
                ]
            )

            process.poll()

            audio_input = ffmpeg.input(audio_filename)
            self._cached_inputs.append(audio_input)

            return (vid, audio_input)
