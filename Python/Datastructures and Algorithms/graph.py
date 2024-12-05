graph ={     
    
     1: [2, 3, None],
     2: [4, None],
     3: [None],
     4: [5, 6, None],
     5: [6, None],
     6: [None]
 }

# creation d'une liste chainee vide

from collections import deque
 
deque() # create empty linked list
deque(['a','b','c'])
print(deque('abc'))
deque([{'data': 'a'}, {'data': 'b'}])

# add and remove element
llist = deque("abcde")
llist.append("f") #add an element from the right side
llist.pop() #remove an element from the right side
print(llist)

# cote gauche
llist.appendleft("z") #add from the lefft side
llist.popleft() #add from the lefft side
llist

# create a queue
from collections import deque
queue = deque()
queue.append("Mary")
queue.append("John")
queue.append("Susan")
print(queue)

#Remove the head element from the linked list, mimicking a real-life queue
queue.popleft()
print(queue)


#Stacks
from collections import deque
history = deque()
#Each new element was added to the head of the linked list
history.appendleft("https://realpython.com/")
history.appendleft("https://realpython.com/pandas-read-write-files/")
history.appendleft("https://realpython.com/python-csv/")




# Python program to
# demonstrate stack implementation
# using queue module

from queue import LifoQueue

# Initializing a stack
stack = LifoQueue(maxsize=3)

# qsize() show the number of elements
# in the stack
print(stack.qsize())

# put() function to push
# element in the stack
stack.put('a')
stack.put('b')
stack.put('c')

print("Full: ", stack.full())
print("Size: ", stack.qsize())

# get() function to pop
# element from stack in
# LIFO order
print('\nElements popped from the stack')
print(stack.get())
print(stack.get())
print(stack.get())

print("\nEmpty: ", stack.empty())
