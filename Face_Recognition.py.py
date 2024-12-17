import cv2

face_cap = cv2.CascadeClassifier("C:/Users/DELL/AppData/Local/Programs/Python/Python313/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")
video_cap = cv2.VideoCapture(0)   # 0 is for runtime capture
while True:
    rat, video_data = video_cap.read()
    col = cv2.cvtColor(video_data, cv2.COLOR_BGR2GRAY)
    
    faces = face_cap.detectMultiScale(
        col,
        scaleFactor = 1.1,
        minNeighbors = 5,
        minSize = (30, 30),
        flags = cv2.CASCADE_SCALE_IMAGE
    )
    
    for(x,y,w,h) in faces:
        cv2.rectangle(video_data, (x, y), (x+w, y+h), (0, 255, 0), 2)   
        
    cv2.imshow("Live_Video", video_data)
    if cv2.waitKey(10) == ord("0"):              # 10 is for the video is eneble for 10 second but here I use ord which gives escape order for 0 value press
        break

video_cap.release()
    