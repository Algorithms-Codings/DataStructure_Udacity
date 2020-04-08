'''
Created on Apr 8, 2020

@author: Rajeswari_S
'''

class Node(object):
    def __init__(self,key,value):
        self.key=key
        self.value=value
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
        self.head=self.head.next
        self.head.prev=None
        
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
            node=self.head
            while node.key!=cnode.key:
                node=node.next 
            prevNode=node.prev
            nextNode=node.next
            
            prevNode.next=node.next
            nextNode.prev=prevNode
            
            self.tail.next=node
            node.prev=self.tail
            node.next=None
            self.tail=node
            #print("CurrNode -> [{0},{1}]".format(cnode.key,cnode.value))            
            #prevNode=cnode.prev
            #print("prevNode -> [{0},{1}]".format(prevNode.key,prevNode.value))            
            #nextNode=cnode.next
            #print("NextNode -> [{0},{1}]".format(nextNode.key,nextNode.value))
            #prevNode.next=cnode.next
            #nextNode.prev=prevNode
            #self.tail.next=cnode
            #cnode.prev=self.tail
            #cnode.next=None
            #self.tail=cnode
    def print(self):
        print("Left to Right->")
        node=self.head
        while node is not None:
            print("[{0},{1}]".format(node.key,node.value))
            node=node.next
        print("Right to Left->")
        node=self.tail
        while node is not None:
            print("[{0},{1}]".format(node.key,node.value))
            node=node.prev
            
        
class LRU_Cache(object):

    def __init__(self, capacity=5):
        # Initialize class variables
        self.MAX_SIZE=capacity
        self.no_elements=0
        self.cache={}
        self.LRU=LinkedList(capacity)   
        pass

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key in self.cache:
            n=self.cache[key]
            self.LRU.changeMostRecentlyItem(n)
            return n.value               
        else:
            return -1        
        pass

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if key in self.cache:
            return
        if self.isCacheFull():
            lNode=self.LRU.getLeastRecentlyItem()
            self.LRU.removeLeastRecentlyItem()
            self.cache.pop(lNode.key)
            self.no_elements-=1            
        n=self.LRU.addMostRecentlyItem(key,value)
        #print("Node -> [{0},{1}]".format(n.key,n.value))            
        #print("prevNode -> [{0},{1}]".format(n.prev.key,n.prev.value))            
        #print("nextNode -> [{0},{1}]".format(n.next.key,n.next.value))            

        self.no_elements+=1
        self.cache[key]=n
        pass
    
    def cacheSize(self):
        return self.no_elements
    def isCacheFull(self):
        return self.no_elements==self.MAX_SIZE
    def print(self):
        self.LRU.print()

our_cache = LRU_Cache(5)

our_cache.set(1, 1);
print("after adding [1,1] ->")
our_cache.print()

our_cache.set(2, 2);
print("after adding [2,2] ->")
our_cache.print()

our_cache.set(3, 3);
print("after adding [3,3] ->")
our_cache.print()

our_cache.set(4, 4);
print("after adding [4,4] ->")
our_cache.print()


print("get 1,",our_cache.get(1))       # returns 1
print("after get 1 ->")
our_cache.print()

print("get 2,",our_cache.get(2))       # returns 2
print("after get 2 ->")
our_cache.print()

print("get 9",our_cache.get(9))      # returns -1 because 9 is not present in the cache
print("after get 9 ->")
our_cache.print()

our_cache.set(5, 5)
print("after adding [5,5] ->")
our_cache.print()

our_cache.set(6, 6)
print("after adding [6,6] ->")
our_cache.print()


print("get 3,",our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
print("after get 3 ->")
our_cache.print()

print("get 2,",our_cache.get(2))       # returns 2
print("after get 2 ->")
our_cache.print()


print("get 6 ,",our_cache.get(6))       # returns 6
print("after get 6 ->")
our_cache.print()


print("get 1 ,",our_cache.get(1))       # returns 1
print("after get 1 ->")
our_cache.print()
