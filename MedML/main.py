from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from uvicorn import run

from keras.models import load_model

import os
from pathlib import Path
from utils.mfcc import extract_mfcc
from utils.resize import resize_mfcc

UPLOAD_PATH = Path() / "uploads"

app = FastAPI()

model_dir = "SERModel.h5"
model = load_model(model_dir)

# pickle_in = open("SER_Pickle.pkl", "rb")
# classifier = pickle.load(pickle_in)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/uploadfiles/")
async def create_upload_files(audiofile: UploadFile):
    data = await audiofile.read()
    save_to = UPLOAD_PATH / audiofile.filename

    with open(save_to, "wb") as f:
        f.write(data)
        print("File saved to", save_to)

    mfcc = extract_mfcc(save_to)
    X = resize_mfcc(mfcc)

    out = model.predict(X)
    print(out)

    return {"out": "out"}


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8001))
    run(app, host="127.0.0.1", port=port)
