import os
import numpy as np
from scipy.io import loadmat, savemat

# 指定包含.mat文件的文件夹路径
folder_path = 'C:\\Users\\weiyan.shi\\Desktop\\WiFi-CSI-Sensing-Benchmark\\20240327'


# 遍历文件夹内的所有文件
for filename in os.listdir(folder_path):
    # 检查文件扩展名是否为.mat
    if filename.endswith('.mat'):
        # 构建完整的文件路径
        file_path = os.path.join(folder_path, filename)
        
        # 加载.mat文件
        data = loadmat(file_path)
        
        # 提取rxCSI字段并进行转置以得到(64, 6000)形状
        rxCSI = data['rxCSI'].T
        
        # 计算幅度（绝对值）和相位
        CSIamp = np.abs(rxCSI)
        CSIphase = np.angle(rxCSI)
        
        # 将数据分割为两部分，每部分大小为(32, 6000)
        CSIamp_parts = np.split(CSIamp, 2, axis=0)
        CSIphase_parts = np.split(CSIphase, 2, axis=0)
        
        # 准备字典用于保存到两个新的.mat文件
        new_data1 = {
            'CSIamp': CSIamp_parts[0],
            'CSIphase': CSIphase_parts[0]
        }
        new_data2 = {
            'CSIamp': CSIamp_parts[1],
            'CSIphase': CSIphase_parts[1]
        }
        
        # 构建新的文件名
        base_filename = os.path.splitext(filename)[0]  # 移除.mat扩展名
        new_file1 = f"{base_filename}_part1.mat"
        new_file2 = f"{base_filename}_part2.mat"

        new_directory = os.path.join(folder_path, 'new')
        if not os.path.exists(new_directory):
            os.makedirs(new_directory)
        
        # 保存为两个新的.mat文件
        savemat(os.path.join(new_directory, new_file1), new_data1)
        savemat(os.path.join(new_directory, new_file2), new_data2)

        print(f"Processed and saved {new_file1} and {new_file2}")
