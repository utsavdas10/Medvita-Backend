from fastapi import FastAPI, UploadFile, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from uvicorn import run

import tensorflow as tf
from keras.models import load_model

import os
import sys
from pathlib import Path
from utils.mfcc import extract_mfcc
from utils.resize import resize_mfcc

from video_processing.lightning import lightning

import cv2
import numpy as np


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# route to upload audio files
@app.post("/uploadfiles/")
async def create_upload_files(audiofile: UploadFile):
    model_dir = "models/SERModel.h5"
    model = load_model(model_dir)
    UPLOAD_PATH = Path() / "uploads" # Path to save the uploaded file

    try:
        data = await audiofile.read() # Read the file
        save_to = UPLOAD_PATH / audiofile.filename # Save the file to the path

        if not os.path.exists(UPLOAD_PATH): # Create the directory if it doesn't exist
            os.makedirs(UPLOAD_PATH)

        try:
            with open(save_to, "wb") as f: # Save the file
                f.write(data)
                print("File saved to", save_to)
        except IOError as e:
            print(f"Error saving file: {e}")
            return {"error": "Error saving file"}

        try:
            mfcc = extract_mfcc(save_to) # extract mfcc
            X = resize_mfcc(mfcc) # resize
        except Exception as e:
            print(f"Error processing file [extracting / resizing mfcc]: {e}")
            return {"error": "Error processing file"}

        os.remove(save_to) #delete the file

        try:
            out = model.predict(X) # predict
        except Exception as e:
            print(f"Error predicting emotion: {e}")
            return {"error": "Error predicting emotion"}

        index = out.argmax() # get the index of the highest value

        emotions = ['angry', 'disgust', 'fear', 'happy', 'neutral', 'ps', 'sad'] 
        emotion = emotions[index]

        return {"out": emotion}

    except Exception as e:
        print(f"Unexpected error: {e}")
        return {"error": "Unexpected error"}



# A WebSocket endpoint to receive and send video frames
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    try:
        await websocket.accept() # Accept the WebSocket connection
        await websocket.send_text("Connected to the server. Send video frames.") # Send a message to the client
        print("Client connected.")

        yoga = await websocket.receive_text() # Receive a message from the client
        print(f"Yoga pose: {yoga}")

        model_dir = "models/3.tflite"
        interpreter = tf.lite.Interpreter(model_path=model_dir) # Load the movenet model
        interpreter.allocate_tensors() # Allocate tensors
        input_details = interpreter.get_input_details() # Get input details
        output_details = interpreter.get_output_details() # Get output details
        print("Model loaded and ready.")


        try:
            while True:
                # Receive a video frame as bytes from the client    
                data = await websocket.receive_bytes()
                if data:
                    try:
                        data = await lightning(data, yoga, interpreter, input_details, output_details)
                        # data = await process_video(data, yoga, interpreter, input_details, output_details)
                    except Exception as e:
                        print(f"Error processing video frame: {e}")
                        break

                    # Send the processed frame back to the client
                    await websocket.send_bytes(data) # Process the video frame and return it as bytes
                else:
                    await websocket.send_bytes(data)

        except WebSocketDisconnect:
            print("Client disconnected.")
            await websocket.close(code=1000)
            

    except Exception as e:
        print(f"Unexpected error: {e}")
        await websocket.close(code=1011)
        


if __name__ == "__main__":
    try:
        port = int(os.environ.get("PORT", 8000))  # Retrieve PORT or default to 4000
    except ValueError:  # Handle invalid PORT values
        print("Invalid PORT environment variable. Using default port 4000.")
        port = 4000
    run(app, host="127.0.0.1", port=port)