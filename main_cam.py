from funcs.camera2 import create_folder, camera_App, get_image_name_with_format, replace_and_rename_image
from funcs.function_img import bbox
import keyboard
import time
from ultralytics import YOLO
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'
import numpy as np

# #camera
def main(num):
    camera_App()
    old_name = get_image_name_with_format(source_folder)
    new_name = 'img'+str(num)+'.jpg'
    replace_and_rename_image(source_folder, dstination_folder3, old_name, new_name)

model = YOLO('C:/Users/liadc/.spyder-py3/file_py/YOLOV8_MOD/runs/detect/yolov8n_custom/weights/best.pt')
Weight = 61.1
source_folder = "C:/Users/liadc/OneDrive/תמונות/סרט צילום"
path_name = "C:/Users/liadc/.spyder-py3/file_py/DATA COLLECTION/DATA1"
dstination_folder = path_name+'/W_fish'+str(Weight)
# dstination_folder = 'C:/Users/liadc/.spyder-py3/file_py/DATA COLLECTION/W_fishtraining' # save file with name fish(num)     
create_folder(dstination_folder)
dstination_folder3 = dstination_folder + '/images'
create_folder(dstination_folder3)
dstination_folder4 = dstination_folder + '/voltage'
create_folder(dstination_folder4)


num = 0
stop=0
x  = input('Enter 0 for exit or 1 to continue:')
while (x == '1'):    
    activation_key = 'space'
    # print(f"Press '{activation_key}' to start the process.")
    # keyboard.wait(activation_key)
    main(num)
    
    path = dstination_folder3 + '/img' +str(num)+'.jpg'
    # time.sleep(1)
    r = bbox(path, model)
    np.save(dstination_folder3 +'/Yolo_cordinate' +str(num)+'.npy', r)
    num = num+1
    # stop+=1
    # print(stop)
    # if stop==3:
    #     break
    x  = input('Enter 0 for exit or 1 to continue:')    
#------------------------------------yolo model
# # # img_path = path_name +'/'+ new_name
# for filename in os.listdir(dstination_folder3):
#     if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
#         path = dstination_folder3 + '/' + filename;
        # bbox(path, model)


# # # image file
# vec_white_pixel = []
# vec_name_file = []
# relevant_image = select_image(dstination_folder,vec_white_pixel,vec_name_file)   
# size_fish = size_fish(dstination_folder, relevant_image)
