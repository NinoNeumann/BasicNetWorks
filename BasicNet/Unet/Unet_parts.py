import torch
import torch.nn as nn


class DoubleConv(nn.Module):
    def __init__(self,in_channels,out_channels,mid_channels=None):
        if not mid_channels:
            mid_channels = out_channels
        self.in_channels = in_channels
        self.doubleConv = nn.Sequential(
            nn.Conv2d(in_channels=self.in_channels,)
        )
        pass
    pass
