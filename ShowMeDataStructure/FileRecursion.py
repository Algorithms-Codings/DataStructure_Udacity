from os.path import isdir
from os.path import isfile
from os import listdir
from os.path import join

def find_files(suffix, path):
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
    files=[]
    #print("path=",path)
    filesFolders=listdir(path)
    for item in filesFolders:
        nPath=join(path + "/" + item)
        if isdir(nPath):
            #print("it is directory")
            ##print("item=",item)
            #print("dir path=",nPath)
            subFolderFiles=find_files(suffix,nPath)
            if subFolderFiles is not None:
                files.extend(subFolderFiles)
        else:
            if(item.endswith(".c")):
                #print("it is file")
                #print("item=",item)
                files.append(nPath)
        
    if len(files)!=0:
        return files
    else:
        return None

files=find_files("c","C:/Users/Rajeswari_S/git/DS_Scramble/ShowMeDataStructure/testdir")
for f in files:
    print(f)