import numpy as np
import cv2
path = '/Volumes/Untitled/Habilelabs_projects/Memorizz AI Collage Project/Final Programs/Final Boarderd images/'
file_type = '.JPG'

kernal= np.ones((5,5), np.uint8)

img1 = cv2.imread(path + '1' + file_type)
img2 = cv2.imread(path + '2' + file_type)
img3 = cv2.imread(path + '3' + file_type)
img4 = cv2.imread(path + '4' + file_type)
img5 = cv2.imread(path + '5' + file_type)
img6 = cv2.imread(path + '6' + file_type)


def hconcat_resize(img_list, interpolation = cv2.INTER_CUBIC):
      # take minimum hights
    h_min = min(img.shape[0] 
                for img in img_list)
      
    # image resizing 
    im_list_resize = [cv2.resize(img,
                       (int(img.shape[1]),
                        h_min), interpolation
                                 = interpolation) 
                      for img in img_list]
      
    # return final image
    return cv2.hconcat(im_list_resize)



def vconcat_resize(img_list, interpolation 
                   = cv2.INTER_CUBIC):
      # take minimum width
    w_min = min(img.shape[1] 
                for img in img_list)
      
    # resizing images
    im_list_resize = [cv2.resize(img,
                      (w_min, int(img.shape[0])),
                                 interpolation = interpolation)
                      for img in img_list]
    # return final image
    return cv2.vconcat(im_list_resize)
  
# function calling
img_v_resize = vconcat_resize([img1, img2, img1])
  
# function calling
img_h_resize = hconcat_resize([img1, img2, img1])


def concat_tile_resize(list_2d, 
                       interpolation = cv2.INTER_CUBIC):
      # function calling for every 
    # list of images
    img_list_v = [hconcat_resize(list_h, 
                                interpolation = cv2.INTER_CUBIC) 
                  for list_h in list_2d]
      
    # return final image
    return vconcat_resize(img_list_v, interpolation=cv2.INTER_CUBIC)
  
# function calling
im_tile_resize = concat_tile_resize([[img1, img2, img3],
                                     [img4, img5, img6]])
  


img9C = cv2.resize(im_tile_resize, (8760, 4180), interpolation = cv2.INTER_AREA)


img9C = cv2.copyMakeBorder(im_tile_resize, 80, 80, 80, 80, cv2.BORDER_CONSTANT, None, [255,255,255])


print("Collage of 6 image Printed")

cv2.imshow('ver', img9C)

cv2.imwrite('/Volumes/Untitled/Habilelabs_projects/Memorizz AI Collage Project/Final Programs/Final useful Collage/Collage of 6 image.JPG', img9C)

cv2.waitKey(0)

cv2.destroyAllWindows()
