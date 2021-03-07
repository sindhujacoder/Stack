from Stack import StackList, StackDeQueue, StackLifoQueue, StackLinkedList

print('Stack using List')
stack = StackList()
for i in range(0, 10):
    stack.add(i)
for each in stack:
  print(each)

print('Stack using dequeue')
stack_dequeue = StackDeQueue()
for i in range(10, 20):
  stack_dequeue.add(i)
for each in stack_dequeue:
  print(each)

print('Stack using LIFOqueue')
stack_lifoqueue = StackLifoQueue(10)
for i in range(20, 30):
  stack_lifoqueue.add(i)
for each in stack_lifoqueue:
  print(each)

print('Stack using LinkedList')
stack_linkedlist = StackLinkedList()
for i in range(30, 40):
  stack_linkedlist.push(i)
print(stack_linkedlist)
print('Top element  with  peek')
print(stack_linkedlist.peek())