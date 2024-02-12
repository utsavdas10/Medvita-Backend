# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 23:27:56 2024

@author: atrij
"""

import cv2
import mediapipe as mp
import time
import math
import numpy as np


class PoseDetector:
    def __init__(self, mode = False,maxHands=1,modelComplexity=1, upBody = False, smooth=True, detectionCon = 0.5, trackCon = 0.5):

        self.mode = mode
        self.maxHands = maxHands
        self.modelComplex = modelComplexity
        self.upBody = upBody
        self.smooth = smooth
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.mode,self.maxHands, self.modelComplex,  self.upBody, self.smooth, self.detectionCon, self.trackCon)



    async def findPose(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        #print(results.pose_landmarks)
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)

        return img



    async def getPosition(self, img, draw=True):
        self.lmList= []
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                #print(id, lm)
                cx, cy = int(lm.x * w), int(lm.y * h)
                self.lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
        return self.lmList



    async def findAngle(self,img,p1,p2,p3, draw=True):

        #finding the landmarks
        x1,y1=self.lmList[p1][1:]
        x2,y2=self.lmList[p2][1:]
        x3,y3=self.lmList[p3][1:]

        #calculating the angle between those landmarks
        angle=math.degrees(math.atan2(y3-y2,x3-x2)-
                         math.atan2(y1-y2,x1-x2))
        
        if angle<0:
            angle+=360

        print(angle)

        if draw:
             cv2.circle(img, (x1, y1), 5, (255, 0, 0), cv2.FILLED)
             cv2.circle(img, (x2, y2), 5, (255, 0, 0), cv2.FILLED)
             cv2.circle(img, (x3, y3), 5, (255, 0, 0), cv2.FILLED)
             cv2.putText(img,str(int(angle)),(x2-50, y2+50),
                        cv2.FONT_HERSHEY_PLAIN, 2, (0,0,255),2)
        return angle