from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from uvicorn import run

from keras.models import load_model

import os
import sys
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

    # Save the file
    data = await audiofile.read()
    save_to = UPLOAD_PATH / audiofile.filename

    with open(save_to, "wb") as f:
        f.write(data)
        print("File saved to", save_to)

    # Extract MFCC
    mfcc = extract_mfcc(save_to)
    X = resize_mfcc(mfcc) # resize

    #delete the file
    os.remove(save_to)

    # Predict
    out = model.predict(X)

    #finding the index of max
    index = out.argmax()


    emotions = ['angry', 'disgust', 'fear', 'happy', 'neutral', 'ps', 'sad']
    emotion = emotions[index]

    return {"out": emotion}


if __name__ == "__main__":
    try:
        port = int(os.environ.get("PORT", 8000))  # Retrieve PORT or default to 4000
    except ValueError:  # Handle invalid PORT values
        print("Invalid PORT environment variable. Using default port 4000.")
        port = 4000
    run(app, host="0.0.0.0", port=port)