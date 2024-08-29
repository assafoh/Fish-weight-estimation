import sys
sys.path.append('C:/Users/liadc/.spyder-py3/file_py/picoscope/function')
from picosdk.ps2000 import ps2000 as ps
from picosdk.functions import assert_pico2000_ok
import ctypes
import numpy as np
from funcs.auto_scop_img import sampling_data
import keyboard
import time
from funcs.pico_scope import select_data
from funcs.camera2 import create_folder 

        
def main(handle, duration, interval,i):
    activation_key = 'space'

    # Wait for the activation key to be pressed
#    keyboard.wait(activation_key)

    # Record the start time

    start_time = time.time()
    end_time = start_time + duration

    while time.time() < end_time:
        Y = sampling_data(preTriggerSamples, postTriggerSamples, chandle)
        data_A[:,i]= Y[0]
        data_B[:,i]= Y[1] 
#        idx = idx + 1
        time.sleep(interval)
    ps.ps2000_close_unit(handle)    
#    keyboard.wait(activation_key)        


start_time_sec = 0.0
preTriggerSamples = 750
postTriggerSamples = 750
path_name = "C:/Users/liadc/.spyder-py3/file_py/DATA COLLECTION/DATA1"

dstination_folder = path_name+'/W_fish'+str(61.1) # save file with name fish(num)     
dstination_folder4 = dstination_folder + '/voltage'

# open_device = ps.ps2000_open_unit()
# assert_pico2000_ok(open_device)
# chandle = ctypes.c_int16(open_device) 
duration = 1
interval = 1
freq = int(duration/interval)-1
# data_A = np.zeros((1500,20))
# data_B = np.zeros((1500,20))
idx = 0
num = [
    "1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
    "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]
activation_key = 'space'

# for i in range(20):
#     print(f"Press '{activation_key}' to start the process.")
#     # keyboard.wait(activation_key)
#     open_device = ps.ps2000_open_unit()
#     assert_pico2000_ok(open_device)
#     chandle = ctypes.c_int16(open_device) 
#     main(chandle,duration,interval,i)
#     print(i)
#
# np.save(dstination_folder4+'/IN.npy', data_A)
# np.save(dstination_folder4+'/OUT.npy', data_B)

# np.save(dstination_folder4+'/IN_fish.npy', data_A)
# np.save(dstination_folder4+'/OUT_fish.npy', data_B)

x  = input('Enter 0 for exit or 1 for fish or 2 for water:')
while True:
    if (x == '1'):
        data_A = np.zeros((1500,20))
        data_B = np.zeros((1500,20))
        for i in range(20):
           
        # keyboard.wait(activation_key)
            open_device = ps.ps2000_open_unit()
            assert_pico2000_ok(open_device)
            chandle = ctypes.c_int16(open_device) 
            main(chandle,duration,interval,i)
            print(i+1)
       
    np.save(dstination_folder4+'/IN_fish.npy', data_A)
    np.save(dstination_folder4+'/OUT_fish.npy', data_B)
    x  = input('Enter 0 for exit or 1 for fish or 2 for water:') 
    if(x == '2'): 
        data_A = np.zeros((1500,12))
        data_B = np.zeros((1500,12))
        for i in range(12):
           
            # keyboard.wait(activation_key)
            open_device = ps.ps2000_open_unit()
            assert_pico2000_ok(open_device)
            chandle = ctypes.c_int16(open_device) 
            main(chandle,duration,interval,i)
            print(i+1)
    np.save(dstination_folder4+'/IN.npy', data_A)
    np.save(dstination_folder4+'/OUT.npy', data_B)
    x  = input('Enter 0 for exit or 1 for fish or 2 for water:') 
    if(x=='0'):
        break

# print("Process ended")    
# AA= np.load('C:/Users/liadc/.spyder-py3/file_py/DATA COLLECTION/DATA1/W_fish25/voltage/OUT_fish.npy')
# BB = np.load('C:/Users/liadc/.spyder-py3/file_py/autumatiom/DATA5/L_OUT.npy')
# vout_0 = str(V_out) 
# file_name = 'value.txt'
# with open(file_name, 'w') as f:
#     f.write(vout_0)
    
# file_name = 'value.txt'
# with open(file_name, 'r') as f:
#     value = f.read()
    
# value = float(value)  

# diff_voltage =  value - V_out 
    
# col = ['Lenght', 'Width', 'voltage', 'Weight']
# data_frame = pd.read_csv("C:/Users/liadc/.spyder-py3/file_py/picoscope/data.csv", usecols=col)
# data_frame.loc[len(data_frame.index)] = [round(max(size_fish),4),round(min(size_fish),4), round(max(relevant_data),4),W_fish] 
# data_frame.to_csv("C:/Users/liadc/.spyder-py3/file_py/picoscope/data.csv")

#create data frame
# df = pd.DataFrame(columns=col)
# df.to_csv("C:/Users/liadc/.spyder-py3/file_py/picoscope/data.csv")