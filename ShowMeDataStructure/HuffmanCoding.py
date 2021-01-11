#completed
'''
Created on Apr 13, 2020

@author: Rajeswari_S
'''

import sys
from comtypes.GUID import binary

class Node(object):
    def __init__(self,char,freq,left=None,right=None,binary=None):
        self.char=char
        self.freq=freq
        self.binary=binary
        self.right=right
        self.left=left

class HuffmanTree(object):
    def __init__(self,data):
        self.root=None
        self.get_frequency(data)
        self.binary={}
        
    def generateTree(self):
       while(len(self.freqList)!=1):
           node1=self.freqList[0]
           node2=self.freqList[1]
           node3=Node("#",node1.freq+node2.freq,node1,node2)            
           self.freqList.remove(node1)
           self.freqList.remove(node2)
           self.freqList.append(node3)
           self.freqList=self.sort_frequency_List()       
       self.root=self.freqList.pop()
       self.assignBinary()
    
    def assignBinary(self):
        self.assignBinaryToNode(self.root,"")  
          
    def assignBinaryToNode(self,node,binary):
         if node is None:
             return
         if(node.char!="#"):
             node.binary=binary
             self.binary[node.char]=binary
         self.assignBinaryToNode(node.left,binary + "0")
         self.assignBinaryToNode(node.right,binary + "1")
    
    def get_frequency(self,rawData):
        self.freqList=[]
        for i in set(rawData):
            n=Node(i, rawData.count(i))
            self.freqList.append(n)
        return self.sort_frequency_List()
    
    def sort_frequency_List(self):
        sorted_freq_list= sorted(self.freqList, key = lambda x: x.freq)
        return sorted_freq_list

   
    def returnNode(self,node,binaryCode):
        if node is None:
            return
        if(node.char!="#"):
            #print("binaryCode=",binaryCode,";decodedString=",node.char)
            return binaryCode,node.char
        for c in binaryCode:            
            if(c=="0"):                
                return self.returnNode(node.left,binaryCode[1:])
            elif(c=="1"):
                return self.returnNode(node.right,binaryCode[1:])
             
    def printSelf(self):
        if self.root is None:
            print("root is emoty")
        else:
            self.printNodeDetails(self.root)
        pass
    
    def printNodeDetails(self,node):
        if node is None:
            return
        self.printNodeDetails(node.left)        
        self.printNodeDetails(node.right)  
        print("------------------------")     
        print("char=",node.char)
        print("freq=",node.freq)
        print("binary=",node.binary)
        print("------------------------") 
        pass
    
    


def huffman_encoding(data):   
    ht=HuffmanTree(data)
    ht.generateTree()
    encodedString=""
    for c in data:
        encodedString=encodedString + ht.binary[c]
    return encodedString,ht       
    pass
    


def huffman_decoding(data,tree):
    decodedString=""
    tempString=""
    while len(data)!=0:
       #print("char=",tree.root.char,";freq=",tree.root.freq)
       data,tempString=tree.returnNode(tree.root,data)
       decodedString=decodedString+tempString
       tempString="" 
    return decodedString
        

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"
    
    #a_great_sentence = "My Name is Surender"


    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    tree=huffman_encoding(a_great_sentence)
    encoded_data, tree = huffman_encoding(a_great_sentence)
    #tree.printSelf()
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))