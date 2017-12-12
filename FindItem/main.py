# Find Item 11/12/17

# Finds a specific template match provided by the user in a larger image, either a preexisting image or a current screenshot

from matplotlib import pyplot as plt
from PIL import ImageGrab
import numpy as np
import time
import cv2

function = input("Read test image or current screen...? [1/2]: ") # User imput here (I thought it was a convenient feature to choose)

if function == '1': # READING TEST IMAGE [Option 1]
    img = cv2.imread('gui.png',0) # Path to image to be searched
    img2 = img.copy() # Make a copy of that image
    original = img.copy()
    template = cv2.imread('cake.png',0) # Path of image to search for
    w, h= template.shape[::-1]

    # All the 6 methods for comparison in a list
    # methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED',
    #             'cv2.TM_SQDIFF_NORMED', 'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF']# in order from greatest to least time

    # We will be using TM_CCORR_NORMED (for me, it proved better results)
    # Feel free to experiment by changing the method below with one of the others listed above
    method = 'cv2.TM_CCORR_NORMED'

    last_time = time.time() # Start a timer to time how long the procces takes
    img = img2.copy()

    # Apply template Matching
    res = cv2.matchTemplate(img,template,eval(method))
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    center = (top_left[0]/2 + w, top_left[1]/2 + h) # Get center location
    print(center) # Print location
    cv2.circle(img, (int(top_left[0] + w/2)), (int(top_left[1] + h/2)), 5, (0, 0, 255), 2) # Draw circle

    img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB) # Convert image color

    cv2.rectangle(img, top_left, bottom_right, (0, 0, 255), 2)

    # cv2.imshow("res", res)
    cv2.imshow("template", template)
    #cv2.imshow("original", original)
    cv2.imshow("Template match", img)

    print('Process took {} seconds '.format(time.time()-last_time)) # Print time info statement using timer

    cv2.waitKey(0) # Wair for esc key
    cv2.destroyAllWindows()
    last_time = time.time() # Reset time


else: # READING CURRENT SCREEN [Option 2]
    
    # DISCLAIMER: The PIL (Python Imaging Library) function ImageGrab might not work on windows. This is the usual Mac/Linux alternative to get a screenshot with python.
    
    print("Sleeping for 2 seconds before activation. Get screen ready.") # Get ready! It will read your current screen, and look for template matches on it.
    time.sleep(2) # Wait a bit

    last_time = time.time() # Start timer for time statement

    # Get screenshot 
    #A lot is squished onto one line here. This will get a screenshot at the bbox location (bounding box) using PIL ImageGrab, convert it into a numpy array for Opencv, and then convert the color to template match.
    img = cv2.cvtColor(np.array(ImageGrab.grab(bbox=(0, 0, 2880, 1800))), cv2.COLOR_BGR2GRAY) # bbox specifies specific region (bbox= x,y,width,height *starts top-left)
    img2 = img.copy() # Make a copy of that screenshot
    original = img.copy()
    template = cv2.imread('cake2.png',0) # Path to template image
    w, h = template.shape[::-1]

    # All the 6 methods for comparison in a list
    # methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED',
    #             'cv2.TM_SQDIFF_NORMED', 'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF']# in order from greatest to least time

    method = 'cv2.TM_CCORR_NORMED' # Same as mentioned above, feel free to change method to one above for different results ('different', not better, mind you)

    last_time = time.time() # Get time from procces
    img = img2.copy()

    # Apply template Matching
    res = cv2.matchTemplate(img,template,eval(method))
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum (different methods listed above will get the size/location differently)
    # Don't worry about it if you don't want to change the method used
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)


    x,y = (int(top_left[0] + w / 2)), (int(top_left[1] + h / 2)) # Get location


    cv2.rectangle(img, top_left, bottom_right, 255, 2) # Draw a rectangle

    cv2.imshow("template", template) # Show the template image

    newx, newy = img.shape[1] / 4, img.shape[0] / 4  # new size (w,h)
    scaled = cv2.resize(img, (int(newx), int(newy))) # REsize the image

    cv2.imshow("Scaled template match", scaled) # Show the scaled image


    print('Process took {} seconds '.format(time.time()-last_time)) # Print time info statement



    print("Object found at top_left = "+str(top_left)+", bottom_right = "+str(bottom_right)+".") # Print location of match
    
    
    cv2.waitKey(0) # Wait for esc key
    cv2.destroyAllWindows()
    last_time = time.time() # Reset time
    
    

