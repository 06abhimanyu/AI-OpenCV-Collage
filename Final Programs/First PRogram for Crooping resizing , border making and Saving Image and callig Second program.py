import cv2
import glob
import os
from subprocess import call
import numpy as np
from numpy.lib.type_check import imag

path = glob.glob("/Volumes/Untitled/Habilelabs_projects/Memorizz AI Collage Project/Random Dataset/*.jpeg")


file_count = len(path)



count = 0
j = 0
z = 0

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
    #pts = np.argwhere(canny>0)
    #y1,x1 = pts.min(axis=0)
    #y2,x2 = pts.max(axis=0)
    ## crop the region
    #img1 = img1[y1:y2, x1:x2]

    width = int(img1.shape[1])
    height = int(img1.shape[0])
    dim = (width, height)

    dimratio = width/height
    hor_path = glob.glob("/Volumes/Untitled/Habilelabs_projects/Memorizz AI Collage Project/Final Programs/Final Boarderd images/Horizontal images/*.JPG")
    hor_file_count = len(hor_path)
 
    dim0_5 = (1005, 2010)
    dim0_5_3 = (3015, 6030) 
    dim0_7 = (1407, 2010)
    dim07__255 =(3025, 4322)
    dim1 = (2010, 2010)
    dim1_15 = (3015, 3015)
    dim1_2 = (2412, 2010)
    dim13_12 = (3618, 3015)
    dim1_5 = (3015, 2010)
    dim1_8 = (3618, 2010)
    dim2 = (4020, 2010)
 
    color = [255, 255, 255]

    if 1.35 < dimratio <= 1.60:
        img = cv2.resize(img1, dim1_5, interpolation = cv2.INTER_AREA)
        #img = img[0:2010, 452:2462]
        #cv2.imshow("img", img)
        #cv2.imwrite("/Volumes/Untitled/Habilelabs projects/Memories Multiple programs/Final Programs to make collages/Final Programs to save collages copy/Final Boarderd images copy/"+str(count)+".JPG", img)
        
        hor_file_count = len(hor_path)
        if file_count == 8 and hor_file_count < 2:
            j+=1
            img = cv2.copyMakeBorder(img, 40, 40, 40, 40, cv2.BORDER_CONSTANT, None, color)
            cv2.imwrite("/Volumes/Untitled/Habilelabs_projects/Memorizz AI Collage Project/Final Programs/Final Boarderd images/Horizontal images/"+str(j)+".JPG", img)

        elif file_count == 5 and hor_file_count < 2:
            j+=1
            img = cv2.copyMakeBorder(img, 40, 40, 40, 40, cv2.BORDER_CONSTANT, None, color)
            cv2.imwrite("/Volumes/Untitled/Habilelabs_projects/Memorizz AI Collage Project/Final Programs/Final Boarderd images/Horizontal images/"+str(j)+".JPG", img)

        elif file_count == 7 and hor_file_count < 4:
            j+=1
            img = cv2.copyMakeBorder(img, 40, 40, 40, 40, cv2.BORDER_CONSTANT, None, color)
            cv2.imwrite("/Volumes/Untitled/Habilelabs_projects/Memorizz AI Collage Project/Final Programs/Final Boarderd images/Horizontal images/"+str(j)+".JPG", img)

        else:
            z+=1
            img = img[0:2010, 452:2462]
            img = cv2.copyMakeBorder(img, 40, 40, 40, 40, cv2.BORDER_CONSTANT, None, color)
            cv2.imwrite("/Volumes/Untitled/Habilelabs_projects/Memorizz AI Collage Project/Final Programs/Final Boarderd images/"+str(z)+".JPG", img)
    
    elif 1.60 < dimratio <= 2.00:
        img = cv2.resize(img1, dim1_8, interpolation = cv2.INTER_AREA)
        #cv2.imshow("img", img)
        #img = cv2.copyMakeBorder(img, 40, 40, 40, 40, cv2.BORDER_CONSTANT, None, color)
        #cv2.imwrite("/Volumes/Untitled/Habilelabs projects/Memories Multiple programs/Final Programs to make collages/Final Programs to save collages copy/Final Boarderd images copy/"+str(z)+".JPG", img)


        hor_file_count = len(hor_path)
        if file_count == 8 and hor_file_count < 2:
            j+=1
            img = img[0:2010, 300:3315]
            img = cv2.copyMakeBorder(img, 40, 40, 40, 40, cv2.BORDER_CONSTANT, None, color)
            cv2.imwrite("/Volumes/Untitled/Habilelabs_projects/Memorizz AI Collage Project/Final Programs/Final Boarderd images/Horizontal images/"+str(j)+".JPG", img)

        elif file_count == 5 and hor_file_count < 2:
            j+=1
            img = img[0:2010, 300:3315]
            img = cv2.copyMakeBorder(img, 40, 40, 40, 40, cv2.BORDER_CONSTANT, None, color)
            cv2.imwrite("/Volumes/Untitled/Habilelabs_projects/Memorizz AI Collage Project/Final Programs/Final Boarderd images/Horizontal images/"+str(j)+".JPG", img)

        elif file_count == 7 and hor_file_count < 4: 
            j+=1
            img = img[0:2010, 300:3315]
            img = cv2.copyMakeBorder(img, 40, 40, 40, 40, cv2.BORDER_CONSTANT, None, color)
            cv2.imwrite("/Volumes/Untitled/Habilelabs_projects/Memorizz AI Collage Project/Final Programs/Final Boarderd images/Horizontal images/"+str(j)+".JPG", img)

        else:
            z+=1
            img = img[0:2010, 1005:3015]
            img = cv2.copyMakeBorder(img, 40, 40, 40, 40, cv2.BORDER_CONSTANT, None, color)
            cv2.imwrite("/Volumes/Untitled/Habilelabs_projects/Memorizz AI Collage Project/Final Programs/Final Boarderd images/"+str(z)+".JPG", img)
    

    elif 2.00 < dimratio:
        img = cv2.resize(img1, dim2, interpolation = cv2.INTER_AREA)
        #img = img[0:2010, 1005:3015]
        #cv2.imshow("img", img)
        #img = cv2.copyMakeBorder(img, 40, 40, 40, 40, cv2.BORDER_CONSTANT, None, color)
        #cv2.imwrite("/Volumes/Untitled/Habilelabs projects/Memories Multiple programs/Final Programs to make collages/Final Programs to save collages copy/Final Boarderd images copy/"+str(z)+".JPG", img)


        hor_file_count = len(hor_path)
        if file_count == 8 and hor_file_count < 2:
            j+=1
            img = img[0:2010, 500:3515]
            img = cv2.copyMakeBorder(img, 40, 40, 40, 40, cv2.BORDER_CONSTANT, None, color)
            cv2.imwrite("/Volumes/Untitled/Habilelabs_projects/Memorizz AI Collage Project/Final Programs/Final Boarderd images/Horizontal images/"+str(j)+".JPG", img)

        elif file_count == 5 and hor_file_count < 2:
            j+=1
            img = img[0:2010, 500:3515]
            img = cv2.copyMakeBorder(img, 40, 40, 40, 40, cv2.BORDER_CONSTANT, None, color)
            cv2.imwrite("/Volumes/Untitled/Habilelabs_projects/Memorizz AI Collage Project/Final Programs/Final Boarderd images/Horizontal images/"+str(j)+".JPG", img)

        elif file_count == 7 and hor_file_count < 4: 
            j+=1
            img = img[0:2010, 500:3515]
            img = cv2.copyMakeBorder(img, 40, 40, 40, 40, cv2.BORDER_CONSTANT, None, color)
            cv2.imwrite("/Volumes/Untitled/Habilelabs_projects/Memorizz AI Collage Project/Final Programs/Final Boarderd images/Horizontal images/"+str(j)+".JPG", img)

        else:
            z+=1
            img = img[0:2010, 1005:3015]
            img = cv2.copyMakeBorder(img, 40, 40, 40, 40, cv2.BORDER_CONSTANT, None, color)
            cv2.imwrite("/Volumes/Untitled/Habilelabs_projects/Memorizz AI Collage Project/Final Programs/Final Boarderd images/"+str(z)+".JPG", img)
    


    elif 1.10 < dimratio <= 1.35:
        img = cv2.resize(img1, dim1_2, interpolation = cv2.INTER_AREA)
        #cv2.imshow("img", img)
        #img = cv2.resize(img1, dim1, interpolation = cv2.INTER_AREA)
        #img = cv2.copyMakeBorder(img, 40, 40, 40, 40, cv2.BORDER_CONSTANT, None, color)
        #cv2.imwrite("/Volumes/Untitled/Habilelabs projects/Memories Multiple programs/Final Programs to make collages/Final Programs to save collages copy/Final Boarderd images copy/"+str(z)+".JPG", img)     

        hor_file_count = len(hor_path)
        if file_count == 8 and hor_file_count < 2 and count > 6:
            j+=1
            img = cv2.resize(img1, dim13_12, interpolation = cv2.INTER_AREA)
            img = img[200:2207, 300:3318]
            img = cv2.copyMakeBorder(img, 40, 40, 40, 40, cv2.BORDER_CONSTANT, None, color)
            cv2.imwrite("/Volumes/Untitled/Habilelabs_projects/Memorizz AI Collage Project/Final Programs/Final Boarderd images/Horizontal images/"+str(j)+".JPG", img)

        elif file_count == 5 and hor_file_count < 2 and count > 3:
            j+=1
            img = cv2.resize(img1, dim13_12, interpolation = cv2.INTER_AREA)
            img = img[200:2207, 300:3318]
            img = cv2.copyMakeBorder(img, 40, 40, 40, 40, cv2.BORDER_CONSTANT, None, color)
            cv2.imwrite("/Volumes/Untitled/Habilelabs_projects/Memorizz AI Collage Project/Final Programs/Final Boarderd images/Horizontal images/"+str(j)+".JPG", img)

        elif file_count == 7 and hor_file_count < 4 and count > 3: 
            j+=1
            img = cv2.resize(img1, dim13_12, interpolation = cv2.INTER_AREA)
            img = img[200:2207, 300:3318]
            img = cv2.copyMakeBorder(img, 40, 40, 40, 40, cv2.BORDER_CONSTANT, None, color)
            cv2.imwrite("/Volumes/Untitled/Habilelabs_projects/Memorizz AI Collage Project/Final Programs/Final Boarderd images/Horizontal images/"+str(j)+".JPG", img)

        else:
            z+=1
            img = img[0:2010, 201:2211]
            img = cv2.copyMakeBorder(img, 40, 40, 40, 40, cv2.BORDER_CONSTANT, None, color)
            cv2.imwrite("/Volumes/Untitled/Habilelabs_projects/Memorizz AI Collage Project/Final Programs/Final Boarderd images/"+str(z)+".JPG", img)
    

    elif dimratio <= 0.60:
        img = cv2.resize(img1, dim0_5, interpolation = cv2.INTER_AREA)
        #cv2.imshow("img", img)
        #img = cv2.copyMakeBorder(img, 40, 40, 40, 40, cv2.BORDER_CONSTANT, None, color)
        #cv2.imwrite("/Volumes/Untitled/Habilelabs projects/Memories Multiple programs/Final Programs to make collages/Final Programs to save collages copy/Final Boarderd images copy/"+str(z)+".JPG", img)

        hor_file_count = len(hor_path)
        if file_count == 8 and hor_file_count < 2 and count > 6:
            j+=1
            img = cv2.resize(img1, dim0_5_3, interpolation = cv2.INTER_AREA)
            img = img[1000:3010, 0:3015]
            img = cv2.copyMakeBorder(img, 40, 40, 40, 40, cv2.BORDER_CONSTANT, None, color)
            cv2.imwrite("/Volumes/Untitled/Habilelabs_projects/Memorizz AI Collage Project/Final Programs/Final Boarderd images/Horizontal images/"+str(j)+".JPG", img)

        elif file_count == 5 and hor_file_count < 2 and count > 3:
            j+=1
            img = cv2.resize(img1, dim0_5_3, interpolation = cv2.INTER_AREA)
            img = img[500:3010, 0:3015]
            img = cv2.copyMakeBorder(img, 40, 40, 40, 40, cv2.BORDER_CONSTANT, None, color)
            cv2.imwrite("/Volumes/Untitled/Habilelabs_projects/Memorizz AI Collage Project/Final Programs/Final Boarderd images/Horizontal images/"+str(j)+".JPG", img)

        elif file_count == 7 and hor_file_count < 4 and count > 3: 
            j+=1
            img = cv2.resize(img1, dim0_5_3, interpolation = cv2.INTER_AREA)
            img = img[500:3010, 0:3015]
            img = cv2.copyMakeBorder(img, 40, 40, 40, 40, cv2.BORDER_CONSTANT, None, color)
            cv2.imwrite("/Volumes/Untitled/Habilelabs_projects/Memorizz AI Collage Project/Final Programs/Final Boarderd images/Horizontal images/"+str(j)+".JPG", img)

        else:
            z+=1
            img = img[500:1507, 0:1005]
            img = cv2.copyMakeBorder(img, 40, 40, 40, 40, cv2.BORDER_CONSTANT, None, color)
            cv2.imwrite("/Volumes/Untitled/Habilelabs_projects/Memorizz AI Collage Project/Final Programs/Final Boarderd images/"+str(z)+".JPG", img)
    

    elif 0.60 < dimratio <= 0.90:
        img = cv2.resize(img1, dim0_7, interpolation = cv2.INTER_AREA)
        #cv2.imshow("img", img)
        #img = cv2.copyMakeBorder(img, 40, 40, 40, 40, cv2.BORDER_CONSTANT, None, color)
        #cv2.imwrite("/Volumes/Untitled/Habilelabs projects/Memories Multiple programs/Final Programs to make collages/Final Programs to save collages copy/Final Boarderd images copy/"+str(z)+".JPG", img)

        hor_file_count = len(hor_path)
        if file_count == 8 and hor_file_count < 2 and count > 6:
            j+=1
            img = cv2.resize(img1, dim07__255, interpolation = cv2.INTER_AREA)
            img = img[800:2810, 5:3020]
            img = cv2.copyMakeBorder(img, 40, 40, 40, 40, cv2.BORDER_CONSTANT, None, color)
            cv2.imwrite("/Volumes/Untitled/Habilelabs_projects/Memorizz AI Collage Project/Final Programs/Final Boarderd images/Horizontal images/"+str(j)+".JPG", img)

        elif file_count == 5 and hor_file_count < 2 and count > 3:
            j+=1
            img = cv2.resize(img1, dim07__255, interpolation = cv2.INTER_AREA)
            img = img[800:2810, 5:3020]
            img = cv2.copyMakeBorder(img, 40, 40, 40, 40, cv2.BORDER_CONSTANT, None, color)
            cv2.imwrite("/Volumes/Untitled/Habilelabs_projects/Memorizz AI Collage Project/Final Programs/Final Boarderd images/Horizontal images/"+str(j)+".JPG", img)

        elif file_count == 7 and hor_file_count < 3 and count > 3: 
            j+=1
            img = cv2.resize(img1, dim07__255, interpolation = cv2.INTER_AREA)
            img = img[2010:2810, 5:3020]
            img = cv2.copyMakeBorder(img, 40, 40, 40, 40, cv2.BORDER_CONSTANT, None, color)
            cv2.imwrite("/Volumes/Untitled/Habilelabs_projects/Memorizz AI Collage Project/Final Programs/Final Boarderd images/Horizontal images/"+str(j)+".JPG", img)

        else:
            z+=1
            img = img[500:1507, 201:1206]
            img = cv2.resize(img1, dim1, interpolation = cv2.INTER_AREA)
            img = cv2.copyMakeBorder(img, 40, 40, 40, 40, cv2.BORDER_CONSTANT, None, color)
            cv2.imwrite("/Volumes/Untitled/Habilelabs_projects/Memorizz AI Collage Project/Final Programs/Final Boarderd images/"+str(z)+".JPG", img)
    

    elif 0.90 < dimratio <= 1.10:

        img = cv2.resize(img1, dim1, interpolation = cv2.INTER_AREA)
        #cv2.imshow("img", img)
        #cropped = img1[y1:y2, x1:x2]
        #img = cv2.resize(img1, dim1, interpolation = cv2.INTER_AREA)
        #img = cv2.copyMakeBorder(img, 40, 40, 40, 40, cv2.BORDER_CONSTANT, None, color)
        #cv2.imwrite("/Volumes/Untitled/Habilelabs projects/Memories Multiple programs/Final Programs to make collages/Final Programs to save collages copy/Final Boarderd images copy/"+str(z)+".JPG", img)
        hor_file_count = len(hor_path)
        if file_count == 8 and hor_file_count < 2 and count > 6:
            j+=1
            img = cv2.resize(img1, dim1_15, interpolation = cv2.INTER_AREA)
            img = img[400:2410, 0:3015]
            img = cv2.copyMakeBorder(img, 40, 40, 40, 40, cv2.BORDER_CONSTANT, None, color)
            cv2.imwrite("/Volumes/Untitled/Habilelabs_projects/Memories Multiple programs/Final Programs to make collages/Final Programs to save collages copy/Final Boarderd images copy/Horizontal images/"+str(j)+".JPG", img)

        elif file_count == 5 and hor_file_count < 2 and count > 3:
            j+=1
            img = cv2.resize(img1, dim1_15, interpolation = cv2.INTER_AREA)
            img = img[400:2410, 0:3015]
            img = cv2.copyMakeBorder(img, 40, 40, 40, 40, cv2.BORDER_CONSTANT, None, color)
            cv2.imwrite("/Volumes/Untitled/Habilelabs_projects/Memorizz AI Collage Project/Final Programs/Final Boarderd images/Horizontal images/"+str(j)+".JPG", img)

        elif file_count == 7 and hor_file_count < 4  and count > 3: 
            j+=1
            img = cv2.resize(img1, dim1_15, interpolation = cv2.INTER_AREA)
            img = img[400:2410, 0:3015]
            img = cv2.copyMakeBorder(img, 40, 40, 40, 40, cv2.BORDER_CONSTANT, None, color)
            cv2.imwrite("//Volumes/Untitled/Habilelabs_projects/Memorizz AI Collage Project/Final Programs/Final Boarderd images/Horizontal images/"+str(j)+".JPG", img)

        else:
            z+=1
            img = cv2.copyMakeBorder(img, 40, 40, 40, 40, cv2.BORDER_CONSTANT, None, color)
            cv2.imwrite("/Volumes/Untitled/Habilelabs_projects/Memorizz AI Collage Project/Final Programs/Final Boarderd images/"+str(z)+".JPG", img)
    
    




call(["python", "/Volumes/Untitled/Habilelabs_projects/Memorizz AI Collage Project/Final Programs/Calling 1 to 9 files to make collage.py"])




"""
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
"""

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
    