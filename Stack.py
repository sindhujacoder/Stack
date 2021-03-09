
#implementation of  stack with list, linked list,  dequeue collection, LIFOqueue

#Deques have O(1) speed for appendleft() and popleft() while lists have O(n) performance for insert(0, value) and pop(0). List append performance is hit and miss because it uses realloc() under the hood

#LIST
class StackList:
    def __init__(self):
        self.stack  = []
        

    def add(self, value):
        #o(n) time complexity
        self.stack.append(value)
  
    def delete(self):
        #o(n) time  complexity
        if len(self.stack):
            return self.stack.pop()
        else:
            return  None
    
    def __iter__(self):
        for i in range(len(self.stack)-1, 0, -1):
            yield self.stack.pop()
            
  
#dequeue collection
from collections import deque
class StackDeQueue:
    def __init__(self):
        self.stack  = deque()

    def add(self, value):
        #o(1) time complexity
        self.stack.append(value)
  
    def delete(self):
        #o(1) time  complexity
        if len(self.stack):
            return self.stack.pop()
        else:
            return  None

    def __iter__(self): 
        for i in range(len(self.stack)-1, 0, -1):
            yield self.stack.pop()
        

#LIFOQueue
from queue import LifoQueue
class StackLifoQueue:
    def __init__(self, size):
        self.stack  = LifoQueue(maxsize=size)
    
    def is_full(self):
        return  self.stack.full()
        
    def length(self):
      return self.stack.qsize() 

    def add(self, value):
        #o(n) time complexity
        if self.stack.full():
            print("Can't add  %d.  Stack Full" %  value)
        self.stack.put(value)
  
    def delete(self):
        #o(n) time  complexity
        if self.stack.empty():
            return None
        
        return self.stack.get()

    def __iter__(self): 
        for i in range(self.stack.qsize() -1, 0, -1):
            yield self.stack.get()
      

#LinkedList Implementation
#with Min Stack implementation
#push, pop , min in o(1)
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
    
class StackMinLinkedList:
    def __init__(self):
        self.head = Node("head")
        self.size = 0
        self.min = []

    def get_size(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
      
    def push(self, value):

        if self.size == 0 or self.min[-1] > value:
            self.min.append(value)

        node = Node(value)
        node.next  = self.head.next
        self.head.next =  node
        self.size += 1
    
    def pop(self):
        temp = self.head.next
        self.head.next =  temp.next

        if len(self.min) >0 and temp.data == self.min[-1]:
            self.min.pop()
            
        self.size -= 1
        return temp.data

    def __str__(self):
      temp = self.head.next
      out = ""
      while(temp != None):
          out = out + str(temp.data) + "->"
          temp = temp.next
      return out
    
    def get_min(self):
        return self.min[-1]

    def peek(self):
        if self.is_empty():
            print("Empty Stack")
        return self.head.next.data
          
        



   