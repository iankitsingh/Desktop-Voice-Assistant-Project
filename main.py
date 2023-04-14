import face_recognition
import cv2
import os
import numpy as np
import os
import speak
import wish_me
import main_jarvis
if __name__ == "__main__":
    try:
        path = "dataset"

        images = []
        class_names = []

        myList = os.listdir(path)

        for names in myList:
            curImg = cv2.imread(f"{path}/{names}")
            images.append(curImg)
            class_names.append(os.path.splitext(names)[0])

        def findEncodings(images):
            encodeList = []
            for img in images:
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                encode = face_recognition.face_encodings(img)[0]
                encodeList.append(encode)
            return encodeList

        encodeListKnown = findEncodings(images)
        print("Please Look At The Camera , Face Verification Is In Process...!! ")
        speak.speak("Collecting Your Face Information , Please Wait")

        cap = cv2.VideoCapture(0)

        while True:
            check, img = cap.read()
            if check == True:
                imgSmall = cv2.resize(img, (0, 0), None, 0.25, 0.25)
                imgSmall = cv2.cvtColor(imgSmall, cv2.COLOR_BGR2RGB)
                facesCurFrame = face_recognition.face_locations(imgSmall)
                encodesCurframe = face_recognition.face_encodings(
                    imgSmall, facesCurFrame)
                for encodeFace, faceLoc in zip(encodesCurframe, facesCurFrame):
                    matches = face_recognition.compare_faces(
                        encodeListKnown, encodeFace)
                    faceDis = face_recognition.face_distance(
                        encodeListKnown, encodeFace)
                    matchIndex = np.argmin(faceDis)
                    if matches[matchIndex]:
                        cap.release()
                        cv2.destroyAllWindows()
                        speak.speak("Face Verification Completed Successfully")
                        wish_me.wishMe()
                        main_jarvis.main_execution()
                        break

                    else:
                        cap.release()
                        cv2.destroyAllWindows()
                        print("Authentication Failed , Please Try Again..!!")

                        speak.speak("Authentication Failed...")
                        speak.speak("Your Acess Has Been Denied...")
                        break

    except Exception as e:
        print(e)
        print("Something Went Wrong In Face detection System, Please Check Face Detection Module...!!")
        speak.speak(
            "Something Went Wrong In Face Detection System ,   Please Check Face Detection Module...")
        pass
