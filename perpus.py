import numpy
import os
from os import *
import matplotlib.pyplot
from matplotlib.pyplot import *
from numpy import *
import cv2
from cv2 import *

__doc__ = cv2.__doc__
__doc__ = os.__doc__
__doc__ = matplotlib.pyplot.__doc__
__doc__ = numpy.__doc__

print("\nMengupgrade pip\n") 
system("python -m pip install --upgrade pip")
print("\nMengambil Library yang diperlukan\n")
system("python -m pip install numpy Arg")
system("python -m pip install opencv-python Arg")
system("python -m pip install opencv-contrib-python Arg")
system("python -m pip install Pillow Arg")
