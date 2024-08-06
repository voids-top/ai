import shutil
import os
import glob
import subprocess
import uuid

out = "../dist/*"
blacklist = ["./CNAME", "./.git", "./push.py"]

for file in glob.glob("./*"):
    if file in blacklist:
        continue
    if os.path.isdir(file):
        shutil.rmtree(file)
    else:
        os.remove(file)

for file in glob.glob(out):
    if os.path.isdir(file):
        shutil.copytree(file, f"./{file.split('/')[-1]}")
    else:
        shutil.copy(file, ".")

subprocess.run("git add .", shell=True)
subprocess.run(f"git commit -m {uuid.uuid4()}", shell=True)
subprocess.run("git push", shell=True)