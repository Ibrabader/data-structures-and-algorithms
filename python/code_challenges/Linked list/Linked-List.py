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
        if index<0 or index> ll.get_length()-1:
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

    # def remove_by_value(self, data):

    #     if self.head is None:
    #         return

    #     if self.head.current_value == data :
    #         self.head = self.head.next_value

    #     itr = self.head
    #     if itr.current_value == None:
    #         return self.head
    #     while itr :
    #         if itr.next_value.current_value == data:
    #             itr.next_value = itr.next_value.next_value
    #             break
    #         itr = itr.next_value

    # Remove first node that contains data
if __name__=="__main__":

    ll=LinkedList()

    # ll.insert_at_begaining(87)
    # ll.insert_at_begaining(87)
    # ll.insert_at_begaining(87)
    # ll.insert_at_begaining(87)
    # ll.insert_at_end(22)
    # ll.insert_at_end(22)
    # ll.insert_at_end(22)
    # item=['ahmad','mohammad','ibrahim','ibrahim222']
    # ll.insert_value(item)
    # # ll.remove_at(3)
    # # ll.inser_at(3,'ggg55g')
    # ll.insert_after_value('ibrahim','new_value')
    # ll.print()
    # print(ll.get_length())
    ll = LinkedList()
    ll.insert_value(["banana","mango","grapes","orange"])
    ll.print()
    ll.insert_after_value("banana","apple") # insert apple after mango
    ll.print()
    # # ll.remove_by_value("orange") # remove orange from linked list
    # ll.print()
    # ll.remove_by_value("figs")
    # ll.print()
    # ll.remove_by_value("grapes")
    # ll.print()

    # ll.remove_by_value("mango")
    # ll.print()

    # ll.remove_by_value("apple")
    # ll.print()
    ll.insertBefore('mango','ibrahim')
    ll.print()













































# class Node:
#    def __init__(self,value):
#        self.value=value
#        self.next=None

# class LinkedList:
#     def __init__(self):
#         self.head=None

#     def append(self,value):
#         node = Node(value)
#         if self.head is None:
#             self.head = node
#         else:
#             current = self.head
#             while current.next != None:
#                   current = current.next
#             current.next = node

#     def insert(self,value):
#         node = Node(value)
#         node.next = self.head
#         self.head = node

#     def includes(self,value):

#         current = self.head
#         while current != None:
#             if current.value==value:
#                 return True
#             current = current.next
#         return False

#     def __str__(self):
#         result = ""
#         if self.head is None:
#             result += None
#         else:
#             current = self.head
#             while(current):
#                 result += " {"+str(current.value)+"  } -> "
#                 current = current.next
#             result += "None"
#             return result


# #in the class work








