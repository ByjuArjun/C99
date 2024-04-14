import os
import shutil

source=input("give sorce")
dest=input("giv destinateion")

source=source+"/"
dest=dest+"/"

list=os.listdir(source)
for a in list:
    shutil.copy((source + a), dest)