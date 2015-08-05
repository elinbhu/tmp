#!/usr/bin/python
import os
import zipfile
zfobj=zipfile.ZipFile("testpython.zip")
for name in zfobj.namelist():
    if name.endswith(".txt"):
       print name+" is deleted!"
    else:
       ext_name=os.path.join("/home/elinbhu/tmp/practice",name)
       ext_dir=os.path.dirname(ext_name)
       if not os.path.exists(ext_dir):
           os.mkdir(ext_dir)
       outfile=open(ext_name,"wb")
       outfile.write(zfobj.read(name))
       outfile.close()
       git_add=os.popen("git add ./practice/*")
       git_status=os.popen("git status")
       print git_status
       

