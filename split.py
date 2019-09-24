## Picked up from Kernel

import shutil
import os

IMG_PATH = r'E:\Github projects\Classification-of-MRI-Scans\resized data'
# split the data by train/val/test
for CLASS in os.listdir(IMG_PATH):
    if not CLASS.startswith('.'):
        IMG_NUM = len(os.listdir(os.path.join(IMG_PATH,CLASS)))
        for (n, FILE_NAME) in enumerate(os.listdir(os.path.join(IMG_PATH,CLASS))):
            print(FILE_NAME)
            img = os.path.join(os.path.join(IMG_PATH,CLASS),FILE_NAME)
            if n < 5:
                shutil.copy(img, os.path.join(os.path.join(r'E:\Github projects\Classification-of-MRI-Scans\resized data\TEST',CLASS.upper()), FILE_NAME + '.jpg'))
            elif n < 0.8*IMG_NUM:
                shutil.copy(img, os.path.join(os.path.join(r'E:\Github projects\Classification-of-MRI-Scans\resized data\TRAIN',CLASS.upper()), FILE_NAME + '.jpg'))
            else:
                shutil.copy(img, os.path.join(os.path.join(r'E:\Github projects\Classification-of-MRI-Scans\resized data\VAL',CLASS.upper()), FILE_NAME + '.jpg'))