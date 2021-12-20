#txt 파일 골라서 삭제하기
import os

dir_name = "/Users/doukkim/Downloads/PhC-C2DH-U373_train/resize_img"
test = os.listdir(dir_name)
for item in test:
    if item.endswith("xml.txt"):
        file_oldname = os.path.join(dir_name, item)
        file_newname = os.path.join(dir_name, item[:item.index(".")] + item[-4:])
        os.rename(file_oldname, file_newname)