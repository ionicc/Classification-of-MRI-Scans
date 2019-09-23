from PIL import Image
import os, sys

path = r'E:\Github projects\Classification-of-MRI-Scans\Data\no'
dest = r'E:\Github projects\Classification-of-MRI-Scans\resized data\no'
dirs = os.listdir(path)
x=1
for item in dirs:
    print(os.path.join(path,item))
    if os.path.isfile(os.path.join(path,item)):
        im = Image.open(os.path.join(path,item))
        f, e = os.path.splitext(os.path.join(path,item))
        print(f)
        imResize = im.resize((200,200), Image.ANTIALIAS)
        print(os.path.join(dest,f+e))
        imResize.save(os.path.join(dest,str(x)) + ' resized.jpg', 'JPEG', quality=90)
        x = x + 1