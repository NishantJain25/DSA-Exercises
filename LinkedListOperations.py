# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Node:
    def __init__(self, data=None,next=None):
        self.data = data
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
        
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
            
        itr.next = Node(data, None)
        
    #insert values from an array into a new linked list
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
            
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
            
        return count
    
    #insert element at index start from 0
    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Index out of bounds")
            
        if index == 0:
            self.insert_at_beginning(data)
            return    
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            
            itr = itr.next
            count += 1
            
    #remove element at index (start from 0)
    def remove_at(self, index):
        
        if index < 0 or index >= self.get_length():
            raise Exception("Index out of bounds")
            
        if index == 0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            
            count += 1
            itr = itr.next
        
    def insert_after_value(self, data, value):
        if self.head is None:
            print("List is empty")
            return
               
        itr = self.head
        while itr:
            if itr.next == None and itr.data != value:
                print("Value not found")
                return
            
            if itr.data == value:
                node = Node(data, itr.next)
                itr.next = node
                break
            
            itr = itr.next
            
    def remove_by_value(self, value):
        if self.head is None:
            print("List is empty")
            return
        
        if self.head.data == value:
            self.head = self.head.next
            return
        
        itr = self.head
        while itr:
            if itr.next is None:
                print("Value not found")
                break
            
            if itr.next.data == value:
                itr.next = itr.next.next
                break
            
            itr = itr.next
    
    def search_iterative(self, value_to_be_searched):
        #return true if present and false if not
        if self.head is None:
            return False
        
        itr =  self.head
        while itr:
            if itr.data == value_to_be_searched:
                return True
            itr = itr.next
        return False
    
    def search_recursive(self, value, head):
        head_node = head
        if head_node is None:
            return False
        
        if head_node.data == value:
            return True
        
        return self.search_recursive(value, head_node.next)

    def print_list(self):
        if self.head is None:
            print('Linked list is empty')
            return
        
        itr = self.head
        llstr = ''
        while itr:
            llstr = llstr + str(itr.data) + '-->'
            itr = itr.next
            
        print(llstr)
        
if __name__ == '__main__':   
    ll = LinkedList()
    
    ll.insert_values(["mango","banana","orange","apple"])
    ll.insert_after_value("grapes","mango")  
    print(ll.search_recursive("appl", ll.head))
    ll.print_list()
