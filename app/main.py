from fastapi import (
    FastAPI,
    UploadFile,
    File,
)


app = FastAPI()


@app.get("/ping")
def ping():
    return {"message": "OK"}

@app.post("/upload")
def upload(file: UploadFile = File(...)):
    try:
        contents = file.file.read()
        with open(file.filename, 'wb') as f:
            f.write(contents)
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()

    return {"message": f"Successfully uploaded {file.filename}"}
