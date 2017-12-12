import cv2
import numpy as np
from matplotlib import pyplot as plt
import pyautogui
import time

img_rgb = cv2.imread('Cakes.png')# The path for the image you are searching goes here.
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)# Convert the color of the image
template = cv2.imread('cake2.png',0)# The path for your template (The image you are searching for) goes here
w, h = template.shape[::-1]

res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)# Run the matchTemplate cv2 function
threshold = .95 # Higher is more accurate, and will yeild less possitives
loc = np.where( res >= threshold)

count = 0
x = []
y = []

for pt in zip(*loc[::-1]): # Find all the matches and organize them into two lists with coordinates
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2) # Draw rectangles on matches

    count = count + 1
    x.append(pt[0] + w/2)
    y.append(pt[1] + h/2)


# Resize the image
scale = 2
(newx, newy) = img_rgb.shape[1] / scale, img_rgb.shape[0] / scale  # new size (w,h)
scaled = cv2.resize(img_rgb, (int(newx), int(newy)))

# Display results
cv2.imshow("Scaled", scaled)#scaled image
cv2.imshow("Image Matches", scaled)#original image

print("Count = {}".format(count))#How many matches found

#Print out locations
counts = 0
while counts <= count-1:
    print("X = " + str(x[counts]) + " Y = " + str(y[counts]))
    pyautogui.moveTo(int(x[counts] / 2), int(y[counts] / 2))
    counts += 1

print("{} cakes found.".format(count))


cv2.waitKey(0) # wait for an esc keypress
cv2.destroyAllWindows()
