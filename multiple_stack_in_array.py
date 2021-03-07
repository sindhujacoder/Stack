#Implement array as three stacks
#Here we use 2 arrays min[] and max[] to represent the lower
#and upper bounds for a stack
#Array s[] stores the elements of the stack
#Array top[] is used to store the top index for each stack
#Variable ns represents the stack number
#Variable size represents the size for each stack in an array
#First we build a function init() to initialize the starting values
#Then we have a function createstack() to create the stack
#Function Push() & Pop() are used to push and pop an element to and from the stack
#Function Display() is used to display the elements in a particular stack
min = []
max = []
top = []

#number of stacks
ns = 3
size = 10
stack = []
size = 50/ns;

def init():
    for i in range(0, 50):
        stack[i] = min[i] = max[i] = 0
        top[i] = -1

def createStack():
    min[0] = -1
    max[0] = size - 1
    top[0] = -1
  
  #min and top of 1,2,3,….th stacks  
    for i in range(1, ns+1):
        min[i] = min[i-1] + size
        top[i] = min[i]
  
  #max of 1,2,3,….th stacks will me min of 2,3,4,….th stack
    for i in range(1, ns+1):
        max[i]= min[i+1];

def push(element, k):
    if top[k-1] == max[k-1]:
        print("Stack no %d is full i.e overflow " % k);
        return
  
    top[k-1] = top[k-1] + 1
    stack[top[k-1]] = element

def pop(k):
    if(top[k-1]==min[k-1]):
        print("Stack no %d is empty i.e underflow" % k)
        return
  
    top[k-1] = top[k-1] - 1

def display(k):
    if top[k-1] == min[k-1]:
        print("Stack no %d is empty" %k)
  
    for j in range(min[k-1]+1, top[k-1]):
        print("%s" % (stack[j]) )
  
if __name__ == "main":
    init()
    createStack()

    push(1,1)
    display(2)



  
  



