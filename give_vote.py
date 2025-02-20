from sklearn.neighbors import KNeighborsClassifier # type: ignore
import cv2
import pickle
import numpy as np
import os
import csv
import time
from datetime import datetime
from win32com.client import Dispatch

def speak(str1):
    speak = Dispatch(("SAPI.SpVoice"))
    speak.Speak(str1)

video = cv2.VideoCapture(0)
facedetect = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

if not os.path.exists('data/'):
    os.makedirs("data/")

with open('data/names.pkl', 'rb') as f:
    LABELS = pickle.load(f)

with open('data/faces_data.pkl', 'rb') as f:
    FACES = pickle.load(f)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(FACES, LABELS)

imgBackground = cv2.imread("background.png")

COL_NAMES = ['NAME', 'VOTE', 'DATE', 'TIME']

# Get background dimensions
bg_height, bg_width, _ = imgBackground.shape

while True:
    ret, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = facedetect.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        crop_img = frame[y:y+h, x:x+w]
        resized_img = cv2.resize(crop_img, (50, 50)).flatten().reshape(1, -1)
        output = knn.predict(resized_img)
        ts = time.time()
        date = datetime.fromtimestamp(ts).strftime("%d-%m-%Y")
        timestamp = datetime.fromtimestamp(ts).strftime("%H:%M-%S")
        exist = os.path.isfile("Votes.csv")
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 1)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (50, 50, 255), 2)
        cv2.rectangle(frame, (x, y-40), (x+w, y), (50, 50, 255), -1)
        cv2.putText(frame, str(output[0]), (x, y-15), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1)
    
    # Resize the frame to fit the screen and dynamically center it
    frame_height, frame_width = 480, 640
    frame = cv2.resize(frame, (frame_width, frame_height))

    # Calculate offsets to center the frame in the background
    x_offset = (bg_width - frame_width) // 2
    y_offset = (bg_height - frame_height) // 2

    # Create a copy of the background and overlay the frame
    imgBackground_copy = imgBackground.copy()
    imgBackground_copy[y_offset:y_offset + frame_height, x_offset:x_offset + frame_width] = frame

    cv2.imshow('frame', imgBackground_copy)
    k = cv2.waitKey(1)

    def check_if_exists(value):
        try:
            with open("Votes.csv", "r") as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    if row and row[0] == value:
                        return True
        except FileNotFoundError:
            print("File not found or unable to open the CSV file.")
        return False

    voter_exist = check_if_exists(output[0])
    if voter_exist:
        speak("YOU HAVE ALREADY CASTED YOUR VOTE")
        break
    if k == ord('1'):
        speak("YOUR VOTE HAS BEEN RECORDED")
        time.sleep(5)
        if exist:
            with open("Votes.csv", "+a") as csvfile:
                writer = csv.writer(csvfile)
                attendance = [output[0], "BJP", date, timestamp]
                writer.writerow(attendance)
        else:
            with open("Votes.csv", "+a") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(COL_NAMES)
                attendance = [output[0], "BJP", date, timestamp]
                writer.writerow(attendance)
        speak("THANK YOU FOR PARTICIPATING IN THE ELECTIONS")
        break
    if k == ord('2'):
        speak("YOUR VOTE HAS BEEN RECORDED")
        time.sleep(5)
        if exist:
            with open("Votes.csv", "+a") as csvfile:
                writer = csv.writer(csvfile)
                attendance = [output[0], "CONGRESS", date, timestamp]
                writer.writerow(attendance)
        else:
            with open("Votes.csv", "+a") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(COL_NAMES)
                attendance = [output[0], "CONGRESS", date, timestamp]
                writer.writerow(attendance)
        speak("THANK YOU FOR PARTICIPATING IN THE ELECTIONS")
        break
    if k == ord('3'):
        speak("YOUR VOTE HAS BEEN RECORDED")
        time.sleep(3)
        if exist:
            with open("Votes.csv", "+a") as csvfile:
                writer = csv.writer(csvfile)
                attendance = [output[0], "TDP", date, timestamp]
                writer.writerow(attendance)
        else:
            with open("Votes.csv", "+a") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(COL_NAMES)
                attendance = [output[0], "TDP", date, timestamp]
                writer.writerow(attendance)
        speak("THANK YOU FOR PARTICIPATING IN THE ELECTIONS")
        break
    if k == ord('4'):
        speak("YOUR VOTE HAS BEEN RECORDED")
        time.sleep(3)
        if exist:
            with open("Votes.csv", "+a") as csvfile:
                writer = csv.writer(csvfile)
                attendance = [output[0], "NOTA", date, timestamp]
                writer.writerow(attendance)
        else:
            with open("Votes.csv", "+a") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(COL_NAMES)
                attendance = [output[0], "NOTA", date, timestamp]
                writer.writerow(attendance)
        speak("THANK YOU FOR PARTICIPATING IN THE ELECTIONS")
        break

video.release()
cv2.destroyAllWindows()
