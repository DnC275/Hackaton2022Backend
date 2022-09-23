import editor.editor as editor_main
import editor.model as model

import pathlib


def main():

    video_schema = model.VideoSchema(
        fragments=[
            model.Fragment(
                video_id="a",
                begin=0,
                end=5,
            ),
            model.Fragment(
                video_id="a",
                begin=120,
                end=125,
            ),
            model.Fragment(
                video_id="a",
                begin=60,
                end=65,
            ),
        ],
        format=".mp4",
    )

    editor = editor_main.Editor(pathlib.Path("./data"))

    out_path = editor.process(video_schema)
    print(out_path)


if __name__ == "__main__":
    main()
