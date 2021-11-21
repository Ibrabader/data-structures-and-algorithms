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

class Cat:
 def __init__(self,anim_name):
        self.name=anim_name
        self.type='cat'
class Dog:
    def __init__(self,anim_name):
        self.name= anim_name
        self.type='dog'


class AnimalShelter:
    def __init__(self):
        self.cat=Queue()
        self.dog=Queue()

    def dequeue(self, pref):
        if pref == 'cat':
            if self.cat.is_empty():
                raise Exception("queue is empty")
            else:
                return self.cat.dequeue()
        elif pref == 'dog':
            if self.dog.is_empty():
                raise Exception("queue is empty")
            else:
                return self.dog.dequeue()
        else:
            None
    def enqueue(self, animal):
        if animal.type =='cat':
            self.cat.enqueue(animal.anim_name)
            return animal
        elif animal.type =='dog':
            self.dog.enqueue(animal.anim_name)
            return animal
        else:
            return ' not dog or cat'
if __name__ == '__main__':

    animalShelter = AnimalShelter()
    dog_1 = Dog("aaa")
    animalShelter.enqueue(dog_1)
    dog2 = Dog("bbb")
    dog3 = Dog("ccc")
    animalShelter.enqueue(dog2)
print(animalShelter.cat)
#   print(animalShelter.cat)
#   print(animalShelter.cat)
#   print(animalShelter.dog[0])
