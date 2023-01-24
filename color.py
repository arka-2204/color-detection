import cv2
import numpy as np
import imutils
import time
video = cv2.VideoCapture("AI Assignment video.mp4")


while True:
    _,frame =video.read()
    frame = imutils.resize(frame, width=900)

    hsv_frame =cv2.cvtColor(frame ,cv2.COLOR_BGR2HSV)
    height ,width ,_ = frame.shape
    #print(height ,width)


    # c1x= int(width/2 +50)
    # c1y = int(height/2 -115)
    # pixel1_center = hsv_frame[c1x,c1y]
    # cv2.circle(frame,(c1x,c1y),50,(255,0,0),3)
    
    

# green
    low_green = np.array([80,72,46])  
    high_green = np.array([93,178,121])
    green_mask = cv2.inRange(hsv_frame, low_green, high_green)
    green = cv2.bitwise_and(frame, frame, mask=green_mask)
    #cv2.imshow("Green_frame",green)

    # yellow
    low_yellow = np.array([23,41,133])
    high_yellow = np.array([40,150,255])
    yellow_mask = cv2.inRange(hsv_frame, low_yellow, high_yellow)
    yellow = cv2.bitwise_and(frame, frame, mask=yellow_mask)
    #cv2.imshow("Green_frame",yellow)

     # orange
    low_orange = np.array([2,87,136])
    high_orange = np.array([7,209,255])
    orange_mask = cv2.inRange(hsv_frame, low_orange, high_orange)
    orange = cv2.bitwise_and(frame, frame, mask=orange_mask)
    #cv2.imshow("orange_frame",orange)

     # white
    low_white = np.array([0,0,168])
    high_white = np.array([172,111,255])
    white_mask = cv2.inRange(hsv_frame, low_white, high_white)
    white = cv2.bitwise_and(frame, frame, mask=white_mask)
    #cv2.imshow("white_frame",white)


    # Creating contour to track orange color
    contours, hierarchy = cv2.findContours(orange_mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)
      
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 300 and area<2000):
            x, y, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(frame, (x, y), 
                                       (x + w, y + h), 
                                       (0, 0, 255), 2)
              
            cv2.putText(imageFrame, "orange ball", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.0,
                        (0, 0, 255))
    
    # Creating contour to track yellow color
    contours, hierarchy = cv2.findContours(yellow_mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)
      
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(frame, (x, y), 
                                       (x + w, y + h), 
                                       (0, 0, 255), 2)
              
            cv2.putText(imageFrame, "yellow ball", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.0,
                        (0, 0, 255))

    # Creating contour to track white color
    contours, hierarchy = cv2.findContours(white_mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)
      
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 4700 and area < 5900):
            x, y, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(frame, (x, y), 
                                       (x + w, y + h), 
                                       (0, 0, 255), 2)
              
            cv2.putText(imageFrame, "white ball", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.0,
                        (0, 0, 255))
            #print(area)
    # Creating contour to track green color
    contours, hierarchy = cv2.findContours(green_mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)
      
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(frame, (x, y), 
                                       (x + w, y + h), 
                                       (0, 0, 255), 2)
              
            cv2.putText(imageFrame, "green ball", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.0,
                        (0, 0, 255))
            




    
    cv2.imshow("check",frame)
    start = time.time()
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    end = time.time()

print(start-end)
    
 
    