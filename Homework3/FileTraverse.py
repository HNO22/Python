import os
import fnmatch
import pickle
import sys
import shutil 

def Traverser():
        list_data=[]
        tuple1=()
        start_dir = "fortune1"
        for dirpath, folder, files in os.walk(start_dir):
                for single_file in files:
                        if fnmatch.fnmatch(single_file, "*txt”):
                                filepath = os.path.abspath(os.path.join(dirpath, single_file))
                                f = open(os.path.join(dirpath, single_file))
                                data1= f.read()
                                tuple1=(os.path,data1)
                                list_data.append(tuple1)
        h.open("raw_data.pickle","bw")
        pickle.dump(list_data,h)
        h.close()


print(filepath)
