#!usr/bin/python
def unzip_file(zipfilename,unziptodir):
    #target:unzip file to target dir
    #zipfilename means the unzipfile's route
    #unziptodir means the unziped file route
    if not os.path.exists(unziptodir):
       os.mkdir(unziptodir,0777)
    zfobj=zipfile.ZipFile(zipfilename)
    for name in zfobj.namelist():
       name=name.replace("\\","/")
       if name.endswith("/"):
          p=os.path.join(unziptodir,name[:-1])
          if os.path.exists(p):
             shutil.rmtree(p)
          os.mkdir(p)
       else:
          ext_filename=os.path.join(unziptodir,name)
          ext_dir=os.path.dirname(ext_filename)
          if not os.path.exists(ext_dir):
              os.mkdir(ext_dir,0777)
          outfile=open(ext_filename,"wb")
          outfile=wirte(zfobj.read(name))
          outfile.close()	
