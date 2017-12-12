
from matplotlib import pyplot as plt
from PIL import ImageGrab
import numpy as np
import pyautogui
import time
import cv2

function = input("Read test image or current screen...? [1/2]: ")

if function == '1':
    img = cv2.imread('gui.png',0)
    img2 = img.copy()
    original = img.copy()
    template = cv2.imread('cake.png',0)
    w, h= template.shape[::-1]

    # All the 6 methods for comparison in a list
    # methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED',
    #             'cv2.TM_SQDIFF_NORMED', 'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF']# in order from greatest to least time

    method = 'cv2.TM_CCORR_NORMED'

    last_time = time.time()
    img = img2.copy()
    #method = eval(meth)

    # Apply template Matching
    res = cv2.matchTemplate(img,template,eval(method))
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    center = (top_left[0]/2 + w, top_left[1]/2 + h)
    print(center)
    cv2.circle(img, (int(top_left[0] + w/2)), (int(top_left[1] + h/2)), 5, (0, 0, 255), 2)

    img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)

    cv2.rectangle(img, top_left, bottom_right, (0, 0, 255), 2)

    # cv2.imshow("res", res)
    cv2.imshow("template", template)
    #cv2.imshow("original", original)
    cv2.imshow("Template match", img)

    print('Process took {} seconds '.format(time.time()-last_time))

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    last_time = time.time()


else:
    print("Sleeping for 2 seconds before activation. Get screen ready.")
    time.sleep(2)

    last_time = time.time()

    img = cv2.cvtColor(np.array(ImageGrab.grab(bbox=(0, 0, 2880, 1800))), cv2.COLOR_BGR2GRAY) # bbox specifies specific region (bbox= x,y,width,height *starts top-left)
    img2 = img.copy()
    original = img.copy()
    template = cv2.imread('cake2.png',0)
    w, h = template.shape[::-1]

    # All the 6 methods for comparison in a list
    # methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED',
    #             'cv2.TM_SQDIFF_NORMED', 'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF']# in order from greatest to least time

    method = 'cv2.TM_CCORR_NORMED'

    last_time = time.time()
    img = img2.copy()
    #method = eval(meth)

    # Apply template Matching
    res = cv2.matchTemplate(img,template,eval(method))
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)


    x,y = (int(top_left[0] + w / 2)), (int(top_left[1] + h / 2))


    cv2.rectangle(img, top_left, bottom_right, 255, 2)

    # cv2.imshow("res", res)
    cv2.imshow("template", template)

    newx, newy = img.shape[1] / 4, img.shape[0] / 4  # new size (w,h)
    scaled = cv2.resize(img, (int(newx), int(newy)))

    #cv2.imshow("Scaled", scaled)
    cv2.imshow("Scaled template match", scaled)


    print('Process took {} seconds '.format(time.time()-last_time))



    print("Object found at top_left = "+str(top_left)+", bottom_right = "+str(bottom_right)+".")

    print("Moving mouse to object at X = "+str(x)+", Y = "+str(y)+".")
    pyautogui.moveTo(x/2, y/2)
