
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
        value = self.front.current
        self.front = self.front.next
        return value

    def is_empty(self):
        return not self.front

    def peek(self):
        if not self.is_empty():
            return self.front.current








if __name__ == "__main__":
    stack = Stack()

    stack.push(1)
    stack.push(12)
    stack.push(13)
    stack.pop()
    stack.pop()
    stack.pop()
    # print(stack.peek())
    print(stack.isEmpty())
