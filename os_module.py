import os
files= os.listdir('path\png')
i=1
for file in files:
    if file.endswith('.jpg'):
        print(file)
    os.rename(f"path\png\{file}",f"path\{i}.jpg")
    i=i+1


