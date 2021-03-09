#Sort a stack such that smallest  elements are on top
#You can use an additional temp stack, but may not copy the elements into any  other data structure such as an array. 
#Stack supports push, pop, peek, isEmpty

from Stack import  StackList

def sort(unsorted_stack):
  sorted_stack = StackList()
  
  while(not unsorted_stack.is_empty()):
      tmp =  unsorted_stack.delete()
      while(not sorted_stack.is_empty() and sorted_stack.peek() > tmp):
          unsorted_stack.add(sorted_stack.delete())
      
      sorted_stack.add(tmp)
      
  while(not sorted_stack.is_empty()):
      unsorted_stack.add(sorted_stack.delete())      

  print('Sorted with minimum on top')
  for each in  unsorted_stack:
      print(each)

