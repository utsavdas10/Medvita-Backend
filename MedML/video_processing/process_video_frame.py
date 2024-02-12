import numpy as np
import cv2
import time 
from video_processing.PoseModule import PoseDetector

detector = PoseDetector()

# Storing the angle data of 6 yoga poses   
angle_data = [
    {'Name': 'tadasan', 'right_arm': 201, 'left_arm': 162, 'right_leg': 177, 'left_leg': 182},
    {'Name': 'vrksana', 'right_arm': 207, 'left_arm': 158, 'right_leg': 180, 'left_leg': 329},
    {'Name': 'balasana', 'right_arm': 155, 'left_arm': 167, 'right_leg': 337, 'left_leg': 335},
    {'Name': 'trikonasana', 'right_arm': 181, 'left_arm': 184, 'right_leg': 176, 'left_leg': 182},
    {'Name': 'virabhadrasana', 'right_arm': 167, 'left_arm': 166, 'right_leg': 273, 'left_leg': 178},
    {'Name': 'adhomukha', 'right_arm': 176, 'left_arm': 171, 'right_leg': 177, 'left_leg': 179}
]


# A function to process the video frame and return it as bytes
async def process_video_frame(data):
    # Convert the binary data to a numpy array
    np_data = np.frombuffer(data, dtype=np.uint8)

    # Decode the image data
    img = cv2.imdecode(np_data, cv2.IMREAD_COLOR)

    # Process the image with PoseDetector
    img = await detector.findPose(img)
    lmList = await detector.getPosition(img, draw=False)

    if len(lmList) != 0:
        try:
            right_arm = await detector.findAngle(img, 12, 14, 16, draw=False)
            left_arm = await detector.findAngle(img, 11, 13, 15, draw=False)
            right_leg = await detector.findAngle(img, 24, 26, 28, draw=False)
            left_leg = await detector.findAngle(img, 23, 25, 27, draw=False)
        except Exception as e:
            print(f"Error calculating angles: {e}")
            return None

        # Iterate through angle_data to find matching yoga pose
        for pose in angle_data:
            if (
                abs(right_arm - pose['right_arm']) < 10 and
                abs(left_arm - pose['left_arm']) < 10 and
                abs(right_leg - pose['right_leg']) < 10 and
                abs(left_leg - pose['left_leg']) < 10
            ):
                cv2.putText(img, pose['Name'], (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                break  # Exit loop once the matching yoga pose is found

    # Encode the processed image back into JPEG format
    _, jpeg = cv2.imencode('.jpg', img)
    if jpeg is not None:
        return jpeg.tobytes()
    else:
        print("Error encoding image")
        return None