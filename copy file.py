import os
import shutil

os.mkdir(r'F:\\algorithm\graph\hw7')
path=r'C:\Users\ThinkPad\Desktop\graph\week5_spanning_trees'
for dir in os.listdir(path):
    file=path+'\\'+dir
    if os.path.isdir(file):
        for subfile in os.listdir(file):
            if subfile.endswith('py'):
                shutil.copyfile(file+'\\'+subfile,'F:\\algorithm\graph\hw7'+'\\'+subfile)












