from types import new_class
class Node :
    def __init__ (self, current_value=None,next_value=None):
        self.current_value=current_value
        self.next_value=next_value
class LinkedList:
    def __init__ (self):
        self.head = None


    def insert_at_begaining(self,current_value):
        node = Node(current_value,self.head)
        self.head = node
    def print(self):
        if self.head is None :
            print('ll is empty')
            return

        itr=self.head
        llstr=''
        while itr:
            llstr += str(itr.current_value) + '--->'
            itr = itr.next_value
        print(llstr)

    def insert_at_end(self,data):
        if self.head is None:
            self.head= Node(data,None)
            return
        itr =self.head
        while itr.next_value:
            itr = itr.next_value
        itr.next_value= Node(data,None)

    def insert_value (self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count=0
        itr=self.head
        while itr :
            count+=1
            itr=itr.next_value
        return count
    # def remove_at(self,index):
    #     if index<0 or index> ll.get_length()-1:
    #         raise Exception ('invalid index')
    #     if index == 0 :
    #         self.head = self.head.next_value

    #     count=0
    #     itr = self.head
    #     while itr :
    #         if count == index-1:
    #             itr.next_value=itr.next_value.next_value
    #             break
    #         itr=itr.next_value
    #         count+=1

    def inser_at(self,index,data):
        if index<0 or index> LinkedList.get_length()-1:
            raise Exception ('invalid index')
        if index == 0 :
            self.head = data

        count=0
        itr = self.head
        while itr :
            if count == index-1:
                node = Node(data,itr.next_value)
                itr.next_value = node
                break
            itr=itr.next_value
            count+=1

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None :
            return


        itr=self.head
        while itr :
            if itr.current_value == data_after :
                itr.next_value = Node(data_to_insert,itr.next_value)
                break

            itr=itr.next_value

    def insertBefore(self,data_before,data_to_insert):
        if self.head is None :
            return


        itr=self.head
        while itr :
            if itr.next_value == data_before :
                itr = Node(data_to_insert,itr.next_value)
                break

            itr=itr.next_value

class HashTable(object):
    def __init__(self, size=1024):
        self.size = size
        self.map = [None]*size

    def hash(self, key):
        sum_of_asccii = 0
        for ch in key:
            asccii_of_ch = ord(ch)
            sum_of_asccii+= asccii_of_ch
        temp_value = sum_of_asccii*19
        hashed_key = temp_value%self.size
        return hashed_key

    def add(self, key, value):
        hashed_key = self.hash(key)
        if not self.map[hashed_key]:
            self.map[hashed_key] = value
        else:
            if isinstance(self.map[hashed_key], LinkedList):
                self.map[hashed_key].add([key,value])
            else:
                chain = LinkedList()
                existing_pair = self.map[hashed_key]
                new_pair =[key,value]
                self.map[hashed_key]=chain
                chain.insert_at_begaining(existing_pair)
                chain.insert_at_begaining(new_pair)

    def get(self, key):
        hashed_key=self.hash(key)
        return self.map[hashed_key]

    def contains(self, key):
        hashed_key=self.hash(key)
        if not self.map[hashed_key]:
            return False
        else:
            if type(  self.map[hashed_key])== list:
                print (True)
                return True
            else:
                current =  self.map[hashed_key].head
            if current!=None:
                while current.next != None:
                    if current.value[0] == key:
                        print (True)
                        return (True)
                    current = current.next
                print ("false")
                return False
