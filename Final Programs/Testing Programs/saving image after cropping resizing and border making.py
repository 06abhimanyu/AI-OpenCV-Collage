import cv2
import glob
import os
from subprocess import call
import numpy as np
from numpy.lib.type_check import imag

path = glob.glob("/Volumes/Untitled/Habilelabs projects/Memories Image Data set/Random Marrige dataset/*.jpeg")

count = 0

for i in path:
    print(i)

    count+=1

    img1 = cv2.imread(i)
    scale_percent = 50 # percent of original size
    width = int(img1.shape[1] * scale_percent / 100)
    height = int(img1.shape[0] * scale_percent / 100)
    dim = (width, height)
    img = cv2.blur(img1, (4,4))
    img = cv2.bilateralFilter(img1, 10, 50, 50)
    canny = cv2.Canny(img1, 250, 200)
    ## find the non-zero min-max coords of canny
    pts = np.argwhere(canny>0)
    y1,x1 = pts.min(axis=0)
    y2,x2 = pts.max(axis=0)
    ## crop the region
    cropped = img1[y1:y2, x1:x2]

    width = int(cropped.shape[1])
    height = int(cropped.shape[0])
    dim = (width, height)

    dimratio = width/height
 
    dim34 = (1425, 2010)
    dim1 = (2010, 2010)
    dim16 = (2840, 2010)


    
    if dimratio <= 0.85:
        img = cv2.resize(cropped, dim34, interpolation = cv2.INTER_AREA)
        img = cv2.copyMakeBorder(img, 40, 40, 40, 40, cv2.BORDER_CONSTANT, None, [255,255,255])
        cv2.imwrite("/Volumes/Untitled/Habilelabs projects/Memories Multiple programs/Final Programs to make collages/Final Programs to save collages copy/Final Boarderd images copy/ver_img_"+str(count)+".JPG", img)

    elif 0.85 < dimratio <= 1.35:
        img = cv2.resize(cropped, dim1, interpolation = cv2.INTER_AREA)
        img = cv2.copyMakeBorder(img, 40, 40, 40, 40, cv2.BORDER_CONSTANT, None, [255,255,255])
        cv2.imwrite("/Volumes/Untitled/Habilelabs projects/Memories Multiple programs/Final Programs to make collages/Final Programs to save collages copy/Final Boarderd images copy/sq_img_"+str(count)+".JPG", img)

    elif 1.35 < dimratio:
        img = cv2.resize(cropped, dim16, interpolation = cv2.INTER_AREA)
        img = cv2.copyMakeBorder(img, 40, 40, 40, 40, cv2.BORDER_CONSTANT, None, [255,255,255])
        cv2.imwrite("/Volumes/Untitled/Habilelabs projects/Memories Multiple programs/Final Programs to make collages/Final Programs to save collages copy/Final Boarderd images copy/hor_img_"+str(count)+".JPG", img)

    #img = cv2.copyMakeBorder(img, 40, 40, 40, 40, cv2.BORDER_CONSTANT, None, [255,255,255])


    #cv2.imwrite("/Volumes/Untitled/Habilelabs projects/Memories Multiple programs/Final Programs to make collages/Final Programs to save collages/Final Boarderd images/"+str(count)+".JPG", img)

    #cv2.imshow('Image', img)
    #cv2.destroyAllWindows()

#call(["python", "/Volumes/Untitled/Habilelabs projects/Memories Multiple programs/Final Programs to make collages/Final Programs to save collages/calling 1 to 9 files to make collage.py"])

"""

file_count = len(path)

print(file_count)
"""




"""
    width = int(cropped.shape[1])
    height = int(cropped.shape[0])
    dim = (width, height)

    dimratio = width/height
 
    dim34 = (1200, 1600)
    dim1 = (2000, 2000)
    dim16 = (1600, 1200)
    dim2 = (2000, 1000)


    if dimratio <= 0.83:
        img = cv2.resize(cropped, dim34, interpolation = cv2.INTER_AREA)

    elif 0.83 < dimratio <= 1.38:
        img = cv2.resize(cropped, dim1, interpolation = cv2.INTER_AREA)

    elif 1.38 < dimratio < 1.8:
        img = cv2.resize(cropped, dim16, interpolation = cv2.INTER_AREA)

    elif dimratio >= 1.8:
        img = cv2.resize(cropped, dim2, interpolation = cv2.INTER_AREA)

"""
    