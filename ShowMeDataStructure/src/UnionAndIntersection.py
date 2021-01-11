#completed
'''
Created on Apr 14, 2020

@author: Rajeswari_S
'''
from argh import interaction
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self,element_list):
        self.head = None
        for i in element_list:
            self.append(i)

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            if(cur_head.next is None):
                out_string += str(cur_head.value)
            else:
                out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string
    
    def convertToSet(self):
        cur_head = self.head
        out_string = set()
        while cur_head:
            out_string.add(cur_head.value)
            cur_head = cur_head.next
        return out_string
    
    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

class UnionAndInterSection(object):
    def __init__(self,list_1,list_2):
            
        if(list_1 is None or list_1==""):
            self.llist_1=LinkedList([])
        else:
            self.llist_1=LinkedList(list_1)
        if(list_2 is None or list_2==""):
            self.llist_2=LinkedList([])
        else:
            self.llist_2=LinkedList(list_2)
        
    def union(self):

        lset1=self.llist_1.convertToSet()
        lset2=self.llist_2.convertToSet()
        lset3=lset1.union(lset2)
        #create resultant linked list
        llist3=LinkedList([])
        for i in lset3:
            llist3.append(i)
        return llist3
    

    def intersection(self):
        # Your Solution Here
        lset1=self.llist_1.convertToSet()
        lset2=self.llist_2.convertToSet()
        inter_set=lset2.intersection(lset1)
        #create resultant linked list
        inter_list=LinkedList([])
        for i in inter_set:
            inter_list.append(i)
        return inter_list

