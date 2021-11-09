class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

    def __add__(self, other):
            return Node(self.value + other.value)

    def __str__(self):
        return str(self.value)

class LinkedList:
    def insert(self,value):
        node = Node(value)
        if self.head:
            node.next = self.head
            self.head = node

    def includes(self,value):
        current = self.head
        value_exists = False

        while current is False:
            if current.data == value:
                value_exists = True
            else:
                current = current.next
            return value_exists

    def __str__(self):
        string = ""
        current = self.head

        while current:
            value = current.value
            if current.next is None:
                string +=f"( {value} ) -> NULL"
                break
            string += f"( {value} ) -> "
            current = current.next
        return string
    def __init__(self):
        self.head=None

    def append(self,value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next != None:
                  current = current.next
            current.next = node

    def insert(self,value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def includes(self,value):

        current = self.head
        while current != None:
            if current.value==value:
                return True
            current = current.next
        return False

    def __str__(self):
        result = ""
        if self.head is None:
            result += None
        else:
            current = self.head
            while(current):
                result += " {"+str(current.value)+"  } -> "
                current = current.next
            result += "None"
            return result


    def insertBefore(self,value,key):
        node = Node(value)
        prev = self.head
        current = self.head
        found = False
        while current:
            if current.value == key:
                prev.next = node
                node.next = current
                found = True
                break
            prev = current
            current = current.next
        if not found:
            raise Exception("key not found")

    def insertAfter(self,value,key):
        node = Node(value)
        current = self.head
        found = False
        while current:
            if current.value == key:
                node.next = current.next
                current.next = node
                found = True
                break
            current = current.next
        if not found:
            raise Exception("key not found")



    def kthFromEnd(self,k):
        if k < 0:
            return "k is negative"
        current = self.head
        lenght = 0
        while current:
            current = current.next
            lenght += 1
        if lenght >= k:
            current = self.head
            for i in range (lenght - k-1):
                current = current.next
        else:
            return "Number of k is bigger than Nodes number!"
        return current




