#completed
'''
Created on Apr 14, 2020

@author: Rajeswari_S
'''
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

def union(llist_1, llist_2):
    # Your Solution Here
    lset1=llist_1.convertToSet()
    lset2=llist_2.convertToSet()
    lset3=lset1.union(lset2)
    #create resultant linked list
    llist3=LinkedList([])
    for i in lset3:
        llist3.append(i)
    return llist3
    pass

def intersection(llist_1, llist_2):
    # Your Solution Here
    lset1=llist_1.convertToSet()
    lset2=llist_2.convertToSet()
    lset3=lset1.intersection(lset2)
    #create resultant linked list
    llist3=LinkedList([])
    for i in lset3:
        llist3.append(i)
    return llist3
    pass


# Test case 1

linked_list_1 = LinkedList([3,2,4,35,6,65,6,4,3,21])
linked_list_2 = LinkedList([6,32,4,9,6,1,11,21,1])
print("*******************TestCase1***************")
print("*******************TestCase1- Union***************")
print (union(linked_list_1,linked_list_2))
print("*******************TestCase1 - Intersetction***************")
print (intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList([3,2,4,35,6,65,6,4,3,23])
linked_list_4 = LinkedList([1,7,8,9,11,21,1])
print("*******************TestCase2***************")
print("*******************TestCase2- Union***************")

print (union(linked_list_3,linked_list_4))
print("*******************TestCase2- Intersection***************")
print (intersection(linked_list_3,linked_list_4))
