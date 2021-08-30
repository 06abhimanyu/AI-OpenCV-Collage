import glob
from subprocess import call

path = glob.glob("/Volumes/Untitled/Habilelabs_projects/Memorizz AI Collage Project/Random Dataset/*.jpeg")

file_count = len(path)

print(file_count)



if file_count == 0:
    print("Please Choose Images")

elif file_count == 1:
    print("1 Image Collage")
    call(["python", "/Volumes/Untitled/Habilelabs_projects/Memorizz AI Collage Project/Final Programs/Memories Collage making for 1.py"])

elif file_count == 2:
    print("2 Image Collage")
    call(["python", "/Volumes/Untitled/Habilelabs_projects/Memorizz AI Collage Project/Final Programs/Memories Collage making for 2.py"])

elif file_count == 3:
    print("3 Image Collage")
    call(["python", "/Volumes/Untitled/Habilelabs_projects/Memorizz AI Collage Project/Final Programs/Memories Collage making for 3.py"])


elif file_count == 4:
    print("4 Image Collage")
    call(["python", "/Volumes/Untitled/Habilelabs_projects/Memorizz AI Collage Project/Final Programs/Memories Collage making for 4.py"])


elif file_count == 5:
    print("5 Image Collage")
    call(["python", "/Volumes/Untitled/Habilelabs_projects/Memorizz AI Collage Project/Final Programs/Memories Collage making for 5.py"])


elif file_count == 6:
    print("6 Image Collage")
    call(["python", "/Volumes/Untitled/Habilelabs_projects/Memorizz AI Collage Project/Final Programs/Memories Collage making for 6.py"])


elif file_count == 7:
    print("7 Image Collage")
    call(["python", "/Volumes/Untitled/Habilelabs_projects/Memorizz AI Collage Project/Final Programs/Memories Collage making for 7.py"])


elif file_count == 8:
    print("8 Image  Collage")
    call(["python", "/Volumes/Untitled/Habilelabs_projects/Memorizz AI Collage Project/Final Programs/Memories Collage making for 8.py"])


elif file_count == 9:
    print("9 Image Collage")
    call(["python", "/Volumes/Untitled/Habilelabs_projects/Memorizz AI Collage Project/Final Programs/Memories Collage making for 9.py"])
