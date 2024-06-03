import torch

import torch.nn as nn


class Unet(nn.Module):
    def __init__(self, images, in_channels):

        # 2 D 的卷积层
        self.conv1_1 = nn.Conv2d(in_channels=in_channels,out_channels=64*in_channels,kernel_size=3,stride=1,padding=0)
        self.conv1_2 = nn.Conv2d(in_channels=64*in_channels,out_channels=64*in_channels,kernel_size=3,stride=1,padding=0)


        pass

    pass
