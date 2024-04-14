import os
import shutil

source=input("source where")
dest=input("destination where")

source=source + "/"
dest=dest + "/"

list=os.listdir(source)
for b in list:
    shutil.move((source+b), dest)