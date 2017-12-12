# TemplateMatching with OpenCV in Python3.6 on Mac

These template matching tests were created on Mac HighSierra with Python 3.6, Pycharm, Opencv, and a lot of snacks.

Find Item uses this template image,

![cake.png](/cake.png)

to search another image for an identical set of pixels.


The matchTemplate function in OpenCV will only return excact pixel matches, which makes it impractical for object detection. It is, however, very good for finding images that will always be the same no matter where they are. For example, 8-bit cake on my desktop wallpaper. Or in Minecraft, where the image never changed from one time to another.

ItemFind will find any given template with no hastle, and if I'm correct, will only return the most accurate result. If no possible result is found, it's going to find the next best thing.

![bar.png](/bar.png)
- The Result from FindItem

Go ham , but remember if these are to work, you will require Opencv installed on your machine and working. These will likely run on a RaspberryPi with little change neccessary. Windows is a different story (if you intend to read the screen directly, and not use a prexisting image).
