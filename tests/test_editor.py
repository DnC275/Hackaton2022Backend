import app.editor.editor as editor_main
import app.editor.model as model

import pathlib


def main():

    video_schema = model.VideoSchema(
        fragments=[
            model.Fragment(
                video_id="a",
                begin=0,
                end=1,
            ),
            model.Fragment(
                video_id="a",
                begin=1,
                end=2,
            ),
            model.Fragment(
                video_id="a",
                begin=2,
                end=3,
            ),
        ],
        format=".mp4",
    )

    editor = editor_main.Editor(pathlib.Path("./data"))

    out_path = editor.process(video_schema)
    print(out_path)


if __name__ == "__main__":
    main()
