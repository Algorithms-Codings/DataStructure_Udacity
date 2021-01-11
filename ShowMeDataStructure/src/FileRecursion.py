#completed
"""
For this problem, the goal is to write code for finding all files under a directory
 (and all directories beneath it) that end with ".c"
"""


from os.path import isdir
from os.path import isfile
from os import listdir
from os.path import join
from os.path import exists
"""
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
"""
class FileRecursion(object):
    def __init__(self):
        return
    def find_files(self,suffix, path):
        if(path is None  or path=="" or suffix is None or suffix==""):
            return None
        if(exists(path)==False):
            return None
    
        files=[] #list of paths
        #print("path=",path)
        filesFolders=listdir(path)
        for item in filesFolders:
            nPath=join(path + "/" + item)
            if isdir(nPath): #if it is directory
            #print("it is directory")
            ##print("item=",item)
            #print("dir path=",nPath)
                subFolderFiles=self.find_files(suffix,nPath) #recursive fn; if given object is directory, call find_files for that sub-directory
                if subFolderFiles is not None: # add founded files paths in the list
                    files.extend(subFolderFiles) 
            else: # if it is file
                if(item.endswith("."+suffix)): #if file ends with expected suffix, appends them in the list
                        #print("it is file")
                        #print("item=",item)
                    files.append(nPath)
        
        if len(files)!=0: #if any file found with expected suffix, return files path, otherwise None
            return files
        else:
            return None

if __name__=='__main__':
    
    fr=FileRecursion()
    files=fr.find_files("c","E:/Udacity_DataStr/DataStructure_Udacity/ShowMeDataStructure/testdir")
    for f in files:
        print(f)