import glob
import os

files = glob.glob("*.*")
files.sort(key=os.path.getmtime)
print("\n".join(files))