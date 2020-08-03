import os
import scipy.io as sio 
import numpy as np
def numpy_to_mat():
    numpy_root = './gt_data/'
    numpy_data = sorted(os.listdir(numpy_root))
    save_root = './gt_data_mat/'
    for data in numpy_data:
        to_mat = np.load(numpy_root+data)
        sio.savemat(save_root+data.split('.')[0]+'.mat',{'gt':to_mat})

if __name__ == "__main__":
    numpy_to_mat()
