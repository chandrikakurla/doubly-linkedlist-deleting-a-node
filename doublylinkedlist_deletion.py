#module for garbage collection
import gc
#node class for creating nodes
class Node:
    def __init__(self,data):
        self.next=None
        self.prev=None
        self.data=data
#linkedlist class
class DoublyLinkedList:
    def __init__(self):
        self.head=None
    #function for inserting newnodes as headnode into doubly linkedlist
    def push(self,newdata):
        newnode=Node(newdata)
        if self.head is None:
            self.head=newnode
            return
        self.head.prev=newnode
        newnode.next=self.head
        self.head=newnode
    #function for printing doubly linkedlist elements
    def print_dllist(self):
        currentnode=self.head
        if currentnode is None:
            print("doubly linkedlist is empty")
            return
        print("doubly linkedlist elements:")
        while(currentnode is not None):
            last=currentnode
            print(currentnode.data)
            currentnode=currentnode.next
        '''#code for printing doubly linkedlist elements in reverse order
        print("doubly linkedlist elements in reverse order:")
        while(last is not None):
            print(last.data)
            last=last.prev'''
    #function for deleting given node in doubly linkedlist
    def delete(self,deletenode):
        if self.head is None or deletenode is None:
            print("deletion is not possible")
            return
        #if given node is headnode 
        if self.head==deletenode:
            self.head=self.head.next
            self.head.prev=None
            gc.collect()
            return
        if deletenode.next is not None:
            deletenode.next.prev=deletenode.prev
        #if deletenode.prev is not None:
        deletenode.prev.next=deletenode.next
        gc.collect()

if __name__=="__main__":
    dllist=DoublyLinkedList()
    dllist.push(5)
    dllist.push(4)
    dllist.push(3)
    dllist.push(2)
    dllist.push(1)
    print("doubly linkedlist before deletion")
    dllist.print_dllist()
    dllist.delete(dllist.head.next.next.next.next)
    print("doubly linkedlist after deletion")
    dllist.print_dllist()



