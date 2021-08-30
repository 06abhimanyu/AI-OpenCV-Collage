import glob, os
os.chdir("/Volumes/Untitled/Habilelabs projects/Memories Multiple programs/Final Programs to make collages/Final Programs to save collages copy/Final Boarderd images copy/")
files = glob.glob("*.JPG")

count = 1

for file in files:
    print(file)

    count =+ 1 


    if file == ("hor_img_"+str(count)+".JPG"):
        print("horizontal file")
        count =+ 1 
        #img = cv2.imread(dir_name+i)
        #cv2.imshow("img", img)

    elif file == ("sq_img_"+str(count)+".JPG"):
        print("Square file")
        count =+ 1 

    elif file == ("ver_img_"+str(count)+".JPG"):
        print("vertical file")
        count =+ 1 