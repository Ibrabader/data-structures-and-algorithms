# import ../stack_and_queue.stack_and_queue.py import

# unable to import file:

class Node:
    def __init__ (self,current,next=None):
        self.current=current
        self.next=None

class Stack:
    def __init__(self,node=None):
        self.top=node

    def push(self,value):
        node = Node(value)
        node.next=self.top
        self.top=node

    def pop(self):
        if self.top == None :
            raise Exception ("Stack is empty")
        value=self.top.current
        self.top = self.top.next
        return value
    def peek(self):
        if self.top is None :
            raise Exception ("Stack is empty")
        return self.top.current


    def isEmpty(self):
        if self.top is None:
            return True
        else:
            return False


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        node = Node(value)
        if self.rear is None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if self.front is None:
            return None
        value = self.front.data
        self.front = self.front.next
        return value

    def is_empty(self):
        return not self.front

    def peek(self):
        if not self.is_empty():
            return self.front.data

class PseudoQueue:
    def __init__(self):
        self.stack1=Stack()
        self.stack2=Stack()

    def enqueue(self,value):
        self.stack1.push(value)
        return value

    def dequeue(self):
        if not self.stack1.top:
            raise Exception("queue is empty")
        while self.stack1.top:
            stack1_value = self.stack1.pop()
            self.stack2.push(stack1_value)

        value=self.stack2.pop()

        while self.stack2.top:
            stack2_value=self.stack2.pop()
            self.stack1.push(stack2_value)

        return value



if __name__=="__main__":


    pseudo_queue=PseudoQueue()

    pseudo_queue.enqueue(1)
    pseudo_queue.enqueue(444)
    pseudo_queue.enqueue('gggg')

    pseudo_queue.enqueue(1)
    pseudo_queue.enqueue(444)
    pseudo_queue.enqueue('gggg')

    pseudo_queue.enqueue(1)
    pseudo_queue.enqueue(444)
    pseudo_queue.enqueue('gggg')

    print(pseudo_queue.dequeue())
    print(pseudo_queue.dequeue())
    print(pseudo_queue.dequeue())
    print(pseudo_queue.dequeue())
    print(pseudo_queue.dequeue())
    print(pseudo_queue.dequeue())

