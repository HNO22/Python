import os
import fnmatch
import pickle

def Traverser():
  data_list=[]
  tuple1=()

  start_dir = "fortune1"
  for dirpath, folder, files in os.walk(start_dir):
    for single_file in files:
      if fnmatch.fnmatch(single_file, "*txt") or fnmatch.fnmatch(single_file, "*log"):
        filepath = os.path.abspath(os.path.join(dirpath, single_file)) 
        tuple1 = (filepath,str(single_file))
        data_list.append(tuple1)
  print(data_list)

  f= open("raw_data.pickle", "bw")
  pickle.dump(data_list, f)
  f.close()
Traverser()