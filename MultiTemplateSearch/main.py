import cv2
import numpy as np
from matplotlib import pyplot as plt
import pyautogui
import time

img_rgb = cv2.imread('Cakes.png')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('cake2.png',0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = .95
loc = np.where( res >= threshold)

count = 0
x = []
y = []

for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

    count = count + 1
    x.append(pt[0] + w/2)
    y.append(pt[1] + h/2)


scale = 2
(newx, newy) = img_rgb.shape[1] / scale, img_rgb.shape[0] / scale  # new size (w,h)
scaled = cv2.resize(img_rgb, (int(newx), int(newy)))

#cv2.imshow("Scaled", scaled)
cv2.imshow("Image Matches", scaled)

print("Count = {}".format(count))

#Print out locations
counts = 0
while counts <= count-1:
    print("X = " + str(x[counts]) + " Y = " + str(y[counts]))
    pyautogui.moveTo(int(x[counts] / 2), int(y[counts] / 2))
    counts += 1

print("{} cakes found.".format(count))


cv2.waitKey(0)
cv2.destroyAllWindows()