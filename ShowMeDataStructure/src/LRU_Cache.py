#completed
'''
Created on Apr 8, 2020

@author: Rajeswari_S
'''

class Node(object):
    def __init__(self,key,value):
        self.value=value
        self.key=key
        self.prev=None
        self.next=None
    
class LinkedList(object):
    def __init__(self,size=5):
        self.head=None #Least recently used key
        self.tail=None #most recently used key
        
    def addMostRecentlyItem(self,key,value): #add element in Linked List whenever  new element is added
        n=Node(key,value)
        if self.head is None:
            self.head=n
            self.tail=self.head
        else:
            prevTail=self.tail
            self.tail.next=n
            self.tail=n
            self.tail.prev=prevTail
        return self.tail
            
    def removeLeastRecentlyItem(self):
        if self.head==None:
            return
        key=self.head.key
        self.head=self.head.next
        self.head.prev=None
        return key
        
    def getMostRecentlyItem(self):
        return self.tail
    def getLeastRecentlyItem(self):
        return self.head
    def changeMostRecentlyItem(self,cnode):
        if cnode==self.tail: #no change if item same as current most MR iteam
            return
        elif cnode==self.head:
            #change the second item of LR item as LR item
                       
            self.tail.next=self.head
            self.tail.next.prev=self.tail
            self.tail=self.tail.next
            
            self.head=self.head.next
            self.head.prev=None
            #move the LR item(head) to MR item (tail)
            self.tail.next=None
            #print("after moving head to tail side")
            #self.print()
        else:            
            node=cnode
            prevNode=node.prev
            nextNode=node.next
            
            prevNode.next=node.next
            nextNode.prev=prevNode
            
            self.tail.next=node
            node.prev=self.tail
            node.next=None
            self.tail=node
                
    def print(self):        
        node=self.head
        while node is not None:
            print("{}-{}".format(node.key,node.value),end=",")
            node=node.next
        
class LRU_Cache(object):

    def __init__(self, capacity=5):
        # Initialize class variables
        self.MAX_SIZE=capacity
        self.no_elements=0
        self.cache={}
        self.LRU=LinkedList(capacity)

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key in self.cache:
            n=self.cache[key]
            self.LRU.changeMostRecentlyItem(n)
            return n.value               
        else:
            return -1        

    def set(self, key,value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
       
        if key in self.cache: #if key is present
            lNode=self.cache[key]
            if(lNode.value!=value): #overwrite the node value for the existing key
                lNode.value=value
                self.cache[key]=lNode
            self.LRU.changeMostRecentlyItem(lNode)
            return
        
        if self.isCacheFull(): #if key is not present and cache is full
            #lNode=self.LRU.getLeastRecentlyItem()
            leastItemKey=self.LRU.removeLeastRecentlyItem() #remove the least item from LRU list
            self.cache.pop(leastItemKey)  #remove the entry from cache
            self.no_elements-=1 #decrease the size by 1
        n=self.LRU.addMostRecentlyItem(key,value)      #add node in LRU as last node     
        self.no_elements+=1 #increase the size by 1
        self.cache[key]=n #add new node entry in cache dictionary
        
    
    def cacheSize(self):
        return self.no_elements
    def isCacheFull(self):
        return self.no_elements==self.MAX_SIZE
    def print(self):
        self.LRU.print()
