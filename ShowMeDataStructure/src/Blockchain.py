#completed
from datetime import datetime

import hashlib
from envs.flappybird.Lib.pickle import NONE

class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()
      self.next = None


    def calc_hash(self):
      sha = hashlib.sha256()
      hash_str = (self.data.encode('utf-8'))
      sha.update(hash_str)
      return sha.hexdigest()
  

    def __repr__(self):
        return str(self.timestamp) + str(" | ") + str(self.data) + str(" | ") + str(self.previous_hash) + str(" | ") + str(self.hash)

class BlockChain(object):
    def __init__(self):
        self.head=None 
        self.tail=None
        self.size=0
    def get_hashValue(self,data):
        node=self.head
        if(node is None):
            return
        while node:
            if(node.data==data):
                return node.hash
            node=node.next
        return None
    def remove(self,data):        
        node=self.head
        if(node is None):
            return
        node_prev=None
        if(node.data==data): #removing root node
            self.head=node.next
            self.head.previous_hash=0
        else:
            while node:
                if(node.data==data):
                    if(node.next is None): #removing node is last node
                        node_prev.next=None
                        
                    else:
                        node.next.previous_hash=node_prev.hash
                        node_prev.next=node.next               
                    return
                node_prev=node
                node=node.next
    def append(self, data):
        if data is None or data=="":
            return
        
        elif(self.head==None):
            self.head=Block(datetime.utcnow(), data, 0)
            self.tail=self.head
        else:
            self.tail.next=Block(datetime.utcnow(), data, self.tail.hash)
            self.tail=self.tail.next
        self.size=self.size+1
        return
    
    def getSize(self):
        return self.size
    
    def toList(self):
        out = []
        block = self.head
        while block:
            out.append([block])
            block = block.next
        return out
