import os
import shutil
import time 

path=input("path to the location to remvoe old files: ")
days=input("delete files before which date?")
timec=(time.time())-1*86400

for fileName in os.listdir(path):
    if os.path.getmtime(os.path.join(path,fileName))<timec:
        if os.path.isfile(os.path.join(path,fileName)):
            print(fileName)
            os.remove(os.path.join(path,fileName))
        elif os.path.isfile(os.path.join(path,fileName)):
            print(fileName)
            shutil.rmtree((os.path.join(path,fileName)))