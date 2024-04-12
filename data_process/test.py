import scipy.io as scio

# dataFile = 'C:\\Users\\weiyan.shi\\Desktop\\WiFi-CSI-Sensing-Benchmark\\20240327\\los_180cm_person_60_0_change_hand_0_t20_csi.mat'

# dataFile1 = 'C:\\Users\\weiyan.shi\\Desktop\\WiFi-CSI-Sensing-Benchmark\\data\\NTU-Fi_HAR\\test_amp\\walk\\walk16.mat'
# data1 = scio.loadmat(dataFile1)

dataFile2 = 'C:\\Users\\weiyan.shi\\Desktop\\WiFi-CSI-Sensing-Benchmark\\data\\Ly-Gesture-20240327\\train\\0\\los_180cm_person_60_0_change_hand_0_t20_csi_part1.mat'
data2 = scio.loadmat(dataFile2)
print(data2.shape)