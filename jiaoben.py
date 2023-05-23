# path = r"D:\git\myself\datasets\train_aug.txt"
# with open(path, 'w+', encoding="utf-8") as f:
#     for i in range(1, 4941):
#         if i < 1000:
#             i = str(i)
#             while len(i) < 4:
#                 i = '0' + i
#         f.write(f"wh{i}\n")
import network
# model = network.modeling.__dict__["deeplabv3plus_mobilenet"](num_classes=6, output_stride=16)

available_models = sorted(name for name in network.modeling.__dict__ if name.islower() and \
                          not (name.startswith("__") or name.startswith('_')) and callable(
    network.modeling.__dict__[name])
                          )
print(available_models)