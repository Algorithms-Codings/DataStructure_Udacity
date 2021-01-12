#completed
'''
Created on Apr 13, 2020

@author: Rajeswari_S
'''

import sys

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
        if(len(self.freqList)==1):
           #self.root=self.freqList.pop()
           #self.root.binary="0"
           #self.binary[self.root.char]="0"
           node1=self.freqList[0]
           node3=Node("#",node1.freq,node1)            
           self.freqList.remove(node1)
           self.freqList.append(node3)
           self.freqList=self.sort_frequency_List() 
        else:    
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
        self.freqList=self.sort_frequency_List()
        #print(self.freqList)
    
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
            print("root is empty")
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
    
    

class HuffmanCoding(object):
    def __init__(self,data):
        self.data=data
    
    def huffman_encoding(self): 
        if(self.data is None or self.data==""):
            self.encodedString=""
            self.ht=""
            return
        ht=HuffmanTree(self.data)
        ht.generateTree()
        encodedString=""
        for c in self.data:
            encodedString=encodedString + ht.binary[c]
        self.encodedString=encodedString
        self.ht=ht       
        pass
    


    def huffman_decoding(self):
        if(self.encodedString is None or self.encodedString=="" or self.ht is None or self.ht ==""):
            self.decodedString= ""
            return
        decodedString=""
        tempString=""
        while len(self.encodedString)!=0:
            #print("char=",tree.root.char,";freq=",tree.root.freq)
            self.encodedString,tempString=self.ht.returnNode(self.ht.root,self.encodedString)
            decodedString=decodedString+tempString
            tempString="" 
        self.decodedString=decodedString
