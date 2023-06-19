# This script prompts the user for a file name and runs an image analysis
# to identify and track red dots in the image. It assigns each red dot a unique ID
# and reports the position and size of each dot. The input file should be an image 
# where red dots that need to be tracked are present. The script uses OpenCV's 
# color filtering and contour detection functionalities to achieve this. 
# The output will be a print statement for each detected red dot with its ID, 
# position (centroid coordinates), and size (contour area).

# By Felipe Galindo

import cv2
import numpy as np
import os

# Set the working directory to the location of this script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Prompt the user for a file name
file_name = input("Enter the file name: ")

# Load the image
image = cv2.imread(file_name)

# Check if the image was loaded successfully
if image is None:
    print(f"Unable to open image file: {file_name}")
    exit()

# Convert to HSV for easier color filtering
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define range for red color
lower_red = np.array([0, 100, 100])
upper_red = np.array([10, 255, 255])

# Filter for red color
mask = cv2.inRange(hsv, lower_red, upper_red)

# Find contours
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Assign IDs and record properties
for i, contour in enumerate(contours):
    # Calculate moments for each contour
    M = cv2.moments(contour)

    # Calculate x,y coordinate of center
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    
    # Calculate area of the contour
    area = cv2.contourArea(contour)
    
    print(f"ID: {i}, Position: ({cX}, {cY}), Size: {area}")




