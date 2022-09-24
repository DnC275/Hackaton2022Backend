import ffmpeg
import pathlib
import uuid

import app.editor.model as model


class Editor:
    def __init__(self, data_path: pathlib.Path):

        self.data_path_ = data_path
        self.out_base_path_ = data_path / 'out'

    def process(self, video_schema: model.VideoSchema) -> pathlib.Path:

        inputs = {
            fragment.video_id: ffmpeg.input(self.data_path_ / fragment.video_id)
            for fragment in video_schema.fragments
        }

        trimed_inputs = [
            _trim(inputs[fragment.video_id], fragment.begin, fragment.end)
            for fragment in video_schema.fragments
        ]

        concated_fragments = ffmpeg.concat(*sum(trimed_inputs, ()), v=1, a=1)

        # TODO: Text, images

        out_id = uuid.uuid4()
        out_path = self.out_base_path_ / f"{out_id.hex}{video_schema.format}"

        concated_fragments.output(str(out_path)).run()

        return out_path


def _trim(input, start, end):

    vid = input.video.trim(start=start, end=end).setpts('PTS-STARTPTS')

    aud = input.audio.filter('atrim', start=start, end=end).filter(
        'asetpts', 'PTS-STARTPTS'
    )

    return (vid, aud)
