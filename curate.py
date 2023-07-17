import os

path = "C:/Users/unni/Downloads/scripts/test"

print("starting...")


for root, dirs, files in os.walk(path):
    for i in files:
        os.rename(os.path.join(root, i), os.path.join(root, i).title() )


for root, dirs, files in os.walk(path):
    for i in files:
        os.rename(os.path.join(root, i), os.path.join(root, i).replace("_", " ") )

for root, dirs, files in os.walk(path):
    for i in files:
        os.rename(os.path.join(root, i), os.path.join(root, i).replace(".Mp4", ".mp4") )


for root, dirs, files in os.walk(path):
    for i in files:
        os.rename(os.path.join(root, i), os.path.join(root, i).replace(".Wmv", ".wmv") )


for root, dirs, files in os.walk(path):
    for i in files:
        os.rename(os.path.join(root, i), os.path.join(root, i).replace(".Log", ".log") )



print("done!")
