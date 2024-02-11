from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from uvicorn import run

from keras.models import load_model

import os
import sys
from pathlib import Path
from utils.mfcc import extract_mfcc
from utils.resize import resize_mfcc

import cv2
from fastapi import WebSocket, WebSocketDisconnect

app = FastAPI()

model_dir = "SERModel.h5"
model = load_model(model_dir)


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
    UPLOAD_PATH = Path() / "uploads"
    data = await audiofile.read()
    save_to = UPLOAD_PATH / audiofile.filename

    if not os.path.exists(UPLOAD_PATH):
        os.makedirs(UPLOAD_PATH)

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


# A function to process the video frame and return it as bytes
def process_video_frame(data):
    # Decode the data as a numpy array
    frame = cv2.imdecode(data, cv2.IMREAD_COLOR)
    # Apply some image processing operations, such as grayscale, blur, etc.
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.GaussianBlur(frame, (7, 7), 0)
    # Encode the processed frame as JPEG and return it as bytes
    _, buffer = cv2.imencode('.jpg', frame)
    return buffer.tobytes()

# A WebSocket endpoint to receive and send video frames
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    print("Client connected.")
    try:
        await websocket.send_text("Hello Motuuu !!!")
        while True:
            # Receive a video frame as bytes from the client
            data = await websocket.receive_bytes()
            if data:
                # Process the video frame and return it as bytes
                data = process_video_frame(data)
                # Send the processed frame back to the client
                await websocket.send_bytes(data)
            else:
                break

    except WebSocketDisconnect:
        print("Client disconnected.")
        await websocket.close(code=1000)
        


if __name__ == "__main__":
    try:
        port = int(os.environ.get("PORT", 8000))  # Retrieve PORT or default to 4000
    except ValueError:  # Handle invalid PORT values
        print("Invalid PORT environment variable. Using default port 4000.")
        port = 4000
    run(app, host="0.0.0.0", port=port)