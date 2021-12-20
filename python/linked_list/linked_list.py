# class LinkedList:
#     """
#     Put docstring here
#     """

#     def __init__(self):
#         # initialization here
#         pass

#     def some_method(self):
#         # method body here
#         pass

import math 

def claculat(x,y):
   
    a=x**2
    b=y**2
    z=math.sqrt(a+b)

    return z

print(claculat(50,60))

def claculat2(hight,rob,alt):
     
def breadth_first(tree):
    output=[]
    queue=Queue()
    if tree.root is None:
        return 'this tree is empty'
    queue.enqueue(tree.root)
    while not queue.isEmpty():
        start=queue.dequeue()
        output.append(start.value)
        if start.left:
            queue.enqueue(start.left)
        if start.right:
            queue.enqueue(start.right)
    return output


