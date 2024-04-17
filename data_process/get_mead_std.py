import os
import glob
import numpy as np
import scipy.io as sio

def calculate_global_mean_std(root_dir, data_key):
    # 找到所有的.mat文件路径
    mat_files = glob.glob(os.path.join(root_dir, '**/*.mat'), recursive=True)

    # 初始化列表以存储所有数据
    all_data = []

    # 遍历.mat文件并收集数据
    for fpath in mat_files:
        data = sio.loadmat(fpath)
        all_data.append(data[data_key].flatten())

    # 将所有数据堆叠起来计算全局平均值和标准差
    all_data_stacked = np.concatenate(all_data)
    global_mean = np.mean(all_data_stacked)
    global_std = np.std(all_data_stacked)

    return global_mean, global_std

# 使用您数据的根目录来调用函数
root_directory = "C:\\Users\\weiyan.shi\\Desktop\\WiFi-CSI-Sensing-Benchmark\\data\\Ly-Gesture-20240327"
data_variable = "CSIamp"
mean, std = calculate_global_mean_std(root_directory, data_variable)
print(f"Global Mean: {mean}")
print(f"Global Std: {std}")





