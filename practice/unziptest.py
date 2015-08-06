#!/usr/bin/python
import os
import zipfile
zfobj=zipfile.ZipFile("myfile.zip")
for name in zfobj.namelist():
    ext_name=os.path.join("/home/elinbhu/python_test/practice",name)
    ext_dir=os.path.dirname(ext_name)
    if not os.path.exists(ext_dir):
       os.mkdir(ext_dir)
    outfile=open(ext_name,"wb")
    outfile.write(zfobj.read(name))
    outfile.close()

