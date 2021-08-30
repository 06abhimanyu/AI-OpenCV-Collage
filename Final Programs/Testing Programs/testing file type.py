
"""
import os
import glob
"""
import cv2
import glob, os
os.chdir("/Volumes/Untitled/Habilelabs projects/Memories Multiple programs/Final Programs to make collages/Final Programs to save collages copy/Final Boarderd images copy/")
files = glob.glob("*.JPG")

count = 0

for file in files:
    #print(file)

    count += 1 


    if file == ("hor_img_1.JPG") or file == ("hor_img_2.JPG") or file == ("hor_img_3.JPG") or file == ("hor_img_4.JPG")or file == ("hor_img_5.JPG") or file == ("hor_img_6.JPG") or file == ("hor_img_7.JPG") or file == ("hor_img_8.JPG") or file == ("hor_img_9.JPG"):
        print(file)
        img = cv2.imread(file)
        #cv2.imshow("img", img)
        #cv2.waitKey()
   
    elif file == ("ver_img_1.JPG") or file == ("ver_img_2.JPG") or file == ("ver_img_3.JPG") or file == ("ver_img_4.JPG")or file == ("ver_img_5.JPG") or file == ("ver_img_6.JPG") or file == ("ver_img_7.JPG") or file == ("ver_img_8.JPG") or file == ("ver_img_9.JPG"):
        print(file)
        img = cv2.imread(file)
        #cv2.imshow("img", img)
        #cv2.waitKey()

    elif file == ("sq_img_1.JPG") or file == ("sq_img_2.JPG") or file == ("sq_img_3.JPG") or file == ("sq_img_4.JPG")or file == ("sq_img_5.JPG") or file == ("sq_img_6.JPG") or file == ("sq_img_7.JPG") or file == ("sq_img_8.JPG") or file == ("sq_img_9.JPG"):
        print(file)
        img = cv2.imread(file)
        #cv2.imshow("img", img)
        #cv2.waitKey()



"""



dir_name = '/Volumes/Untitled/Habilelabs projects/Memories Multiple programs/Final Programs to make collages/Final Programs to save collages copy/Final Boarderd images copy/'
# Get list of all files in a given directory sorted by name
list_of_files = sorted( filter( lambda x: os.path.isfile(os.path.join(dir_name, x)),
                        os.listdir(dir_name) ) )


count = 0

for i in list_of_files:
    print(i)

    count += 1 

    if i == "hor_img_"+str(count)+".JPG":
        print("horizontal file")
        #img = cv2.imread(dir_name+i)
        #cv2.imshow("img", img)

    elif i == "sq_img_"+str(count)+".JPG":
        print("Square file")

    elif i == "ver_img_"+str(count)+".JPG":
        print("vertical file")



    
      
   

cv2.waitKey()

"""


# All files ending with .txt with depth of 2 folder
"""

for i in path:
    print(i)

    count+=1

    img1 = cv2.imread(i)
    """"""
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
"""