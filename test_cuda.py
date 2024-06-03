import torch

if torch.cuda.is_available():
    print("已经安装正确的cuda版本")
else:
    print("可能是cuda版本不正确。")
