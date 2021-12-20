from PIL import Image
import os

dir_name_list = ["/Users/doukkim/Downloads/PhC-C2DH-U373_train/01/", "/Users/doukkim/Downloads/PhC-C2DH-U373_train/02/"]
for i, dir_name in enumerate(dir_name_list):
    test = os.listdir(dir_name)
    for j, item in enumerate(test):
        if item.endswith(".tif"):
            img = Image.open(os.path.join(dir_name, item))
            img_resize = img.resize((512, 512))
            img_resize.save(f"/Users/doukkim/Downloads/PhC-C2DH-U373_train/resize_img/t{i}_{j}_resized.jpg")