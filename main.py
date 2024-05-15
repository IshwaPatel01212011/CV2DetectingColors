import cv2
import numpy as np

treasure = cv2.VideoCapture("Lesson 7 /images/green.mp4")
#treasure = treasure.read()
#print(treasure)

for i in range(60):
    return_val, bg = treasure.read()

#cv2.imshow("Background",bg)
#cv2.waitKey(0)

while treasure.isOpened():
    return_val,img = treasure.read()
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    Lower_g = np.array([104,153,70])
    Upper_g = np.array([30,30,0])
    mask_1 = cv2.inRange(hsv,Lower_g, Upper_g)
    Lower_g = np.array([50,100,100])
    Upper_g = np.array([70,255,255])
    mask_2 = cv2.inRange(hsv,Lower_g, Upper_g)
    mask = mask_1 + mask_2
    mask = cv2.morphologyEx(mask,cv2.MORPH_OPEN, np.ones((3,3),np.uint8),iterations = 2)
    mask = cv2.dilate(mask,np.ones((3,3),np.uint8),iterations = 1)
    mask_3 = cv2.bitwise_not(mask)
    park_1 = cv2.bitwise_and(bg, bg, mask = mask)
    park_2 = cv2.bitwise_and(img,img,mask = mask_3)
    final = cv2.addWeighted(park_1, 1, park_2, 1, 0)
    cv2.imshow("Images", final)
    cv2.waitKey(0)
