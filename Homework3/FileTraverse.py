import os
import fnmatch

def Traverser():
  data_list=[]
  tuple1=()

  start_dir = "fortune1"
  for dirpath, folder, files in os.walk(start_dir):
    for single_file in files:
      if fnmatch.fnmatch(single_file, "*txt") or fnmatch.fnmatch(single_file, "*log"):
        filepath = os.path.abspath(os.path.join(dirpath, single_file))
        
        f=open(filepath)
        data1=f.read()
        f.close()    
        tuple1 = (filepath,data1)
        data_list.append(tuple1)


        print(data_list)
Traverser()