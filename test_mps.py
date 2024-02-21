import torch
if torch.backends.mps.is_available():
    mps_device = torch.device("mps")
    x = torch.ones(1, device=mps_device)
    print (x)
else:
    print ("MPS device not found.")

# mps_device = torch.device("mps")
#
# # Create a Tensor directly on the mps device
# x = torch.ones(5, device=mps_device)
# # Or
# x = torch.ones(5, device="mps")
#
# # Any operation happens on the GPU
# y = x * 2
#
# # Move your model to mps just like any other device
# model = YourFavoriteNet()
# model.to(mps_device)
#
# # Now every call runs on the GPU
# pred = model(x)
