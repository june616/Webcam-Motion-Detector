import cv2


first_frame=None

video=cv2.VideoCapture(0)

while True:
    check, frame = video.read()
    # frame variable is converted to a grayscale version
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # Blur the gray image
    gray=cv2.GaussianBlur(gray,(21,21),0)

    if first_frame is None:
        first_frame=gray
        continue

    delta_frame=cv2.absdiff(first_frame,gray)
    thresh_frame=cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame=cv2.dilate(thresh_frame, None, iterations=2)
    (cnts,_)=cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Filter out these contours, keep only contour area > 10000 pixels
    for contour in cnts:
        if cv2.contourArea(contour) < 10000:
            continue
        (x, y, w, h)=cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 3)

    cv2.imshow("Gray Frame",gray)
    cv2.imshow("Delta Frame",delta_frame)
    cv2.imshow("Threshold Frame",thresh_frame)
    cv2.imshow("Color Frame",frame)

    key=cv2.waitKey(1)
