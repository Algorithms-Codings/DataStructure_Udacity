#completed
from datetime import datetime

import hashlib

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

class BlockChain:
    def __init__(self):
        self.head=None #root block
        self.tail=None
    def append(self, data):
        if data is None or data=="":
            return
        
        elif(self.head==None):
            self.head=Block(datetime.utcnow(), data, 0)
            self.tail=self.head
        else:
            self.tail.next=Block(datetime.utcnow(), data, self.tail.hash)
            self.tail=self.tail.next
        return
    
    def toList(self):
        out = []
        block = self.head
        while block:
            out.append([block])
            block = block.next
        return out

bl=BlockChain()
bl.append( "First Data")
bl.append("Second Data")
bl.append( "Third Data")
print(bl.toList())