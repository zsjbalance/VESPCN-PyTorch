# Below are imports just for testing
from option import args
import cv2, imageio
from data.vsrdata import VSRData
"""
Original test setting: 5 videos with 30 frames inside each directory
length of frame sequence = 4
batch_size = 2
"""
'''
if __name__ == '__main__':
    if args.template == 'SY':
        vsr = VSRData(args, name='CDVL_Video', train=False)
    else:
        vsr = VSRData(args)
    print(len(vsr.data_hr))  # 5
    print(len(vsr.data_lr))  # 5
    print(vsr.data_hr[1].shape)  # (4,1080,1920,3)
    print(vsr.data_lr[1].shape)  # (4, 360, 640, 3)
    img_samples = []
    for i in range(args.n_sequence):
        imageio.imwrite('hr_{}.jpg'.format(i), vsr.data_hr[0][i, :])
        imageio.imwrite('lr_{}.jpg'.format(i), vsr.data_lr[0][i, :])
    print(len(vsr[0][0]))  # 4
    print(vsr[0][0][0].shape)  # torch.Size([3,17,17])
    print(len(vsr[0][1]))  # 4
    print(vsr[0][1][0].shape)  # torch.Size([3,51,51])
    print(vsr[0][2])  # ['00001', '00002', '00003', '00004']
'''

    
import torch.nn.functional as F
import torch.optim as optim
import torch
import torchvision
from PIL import Image
import numpy as np

img = Image.open('./frame1.png')
img = np.array(img)
img = np.array([img]).astype("float64")
b = torch.from_numpy(img)
b = b.permute(0, 3, 1, 2)
print(b.size())
# b has the size (1, 3, 360, 640)
flow = torch.rand(1, 360, 640 , 2)
b = Variable(b)
flow = Variable(flow)
compensated = F.grid_sample(b, flow)
print(compensated.shape)