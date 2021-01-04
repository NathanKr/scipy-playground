import scipy.io as sio
from os.path import join 
import os

current_dir = os.path.abspath(".")
data_dir = join(current_dir, 'data')
file_name = join(data_dir,"ex5data1.mat")
mat_dict = sio.loadmat(file_name)
print(len(mat_dict))
print(mat_dict)
print(mat_dict["__header__"])
print(mat_dict["__version__"])
print(mat_dict["__globals__"])
print(mat_dict["X"])
print(mat_dict["y"])
print(mat_dict["Xtest"])
print(mat_dict["ytest"])
print(mat_dict["Xval"])
print(mat_dict["yval"])
