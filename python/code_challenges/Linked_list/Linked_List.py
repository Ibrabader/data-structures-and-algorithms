# class Node :
#     def __init__ (self, current_value=None,next_value=None):
#         self.current_value=current_value
#         self.next_value=next_value

# class LinkedList:
#     def __init__ (self):
#         self.head = None


#     def insert_at_begaining(self,current_value):
#         node = Node(current_value,self.head)
#         self.head = node
#     def print(self):
#         if self.head is None :
#             print('ll is empty')
#             return

#         itr=self.head
#         llstr=''
#         while itr:
#             llstr += str(itr.current_value) + '--->'
#             itr = itr.next_value
#         print(llstr)

#     def insert_at_end(self,data):
#         if self.head is None:
#             self.head= Node(data,None)
#             return
#         itr =self.head
#         while itr.next_value:
#             itr = itr.next_value
#         itr.next_value= Node(data,None)

#     def insert_value (self,data_list):
#         self.head = None
#         for data in data_list:
#             self.insert_at_end(data)

#     def get_length(self):
#         count=0
#         itr=self.head
#         while itr :
#             count+=1
#             itr=itr.next_value
#         return count
#     # def remove_at(self,index):
#     #     if index<0 or index> ll.get_length()-1:
#     #         raise Exception ('invalid index')
#     #     if index == 0 :
#     #         self.head = self.head.next_value

#     #     count=0
#     #     itr = self.head
#     #     while itr :
#     #         if count == index-1:
#     #             itr.next_value=itr.next_value.next_value
#     #             break
#     #         itr=itr.next_value
#     #         count+=1

#     def inser_at(self,index,data):
#         if index<0 or index> ll.get_length()-1:
#             raise Exception ('invalid index')
#         if index == 0 :
#             self.head = data

#         count=0
#         itr = self.head
#         while itr :
#             if count == index-1:
#                 node = Node(data,itr.next_value)
#                 itr.next_value = node
#                 break
#             itr=itr.next_value
#             count+=1

#     def insert_after_value(self, data_after, data_to_insert):
#         if self.head is None :
#             return


#         itr=self.head
#         while itr :
#             if itr.current_value == data_after :
#                 itr.next_value = Node(data_to_insert,itr.next_value)
#                 break

#             itr=itr.next_value

#     def insertBefore(self,data_before,data_to_insert):
#         if self.head is None :
#             return


#         itr=self.head
#         while itr :
#             if itr.next_value == data_before :
#                 itr = Node(data_to_insert,itr.next_value)
#                 break

#             itr=itr.next_value

#     # def remove_by_value(self, data):

#     #     if self.head is None:
#     #         return

#     #     if self.head.current_value == data :
#     #         self.head = self.head.next_value

#     #     itr = self.head
#     #     if itr.current_value == None:
#     #         return self.head
#     #     while itr :
#     #         if itr.next_value.current_value == data:
#     #             itr.next_value = itr.next_value.next_value
#     #             break
#     #         itr = itr.next_value

#     # Remove first node that contains data
# if __name__=="__main__":

#     ll=LinkedList()

#     # ll.insert_at_begaining(87)
#     # ll.insert_at_begaining(87)
#     # ll.insert_at_begaining(87)
#     # ll.insert_at_begaining(87)
#     # ll.insert_at_end(22)
#     # ll.insert_at_end(22)
#     # ll.insert_at_end(22)
#     # item=['ahmad','mohammad','ibrahim','ibrahim222']
#     # ll.insert_value(item)
#     # # ll.remove_at(3)
#     # # ll.inser_at(3,'ggg55g')
#     # ll.insert_after_value('ibrahim','new_value')
#     # ll.print()
#     # print(ll.get_length())
#     ll = LinkedList()
#     ll.insert_value(["banana","mango","grapes","orange"])
#     ll.print()
#     ll.insert_after_value("banana","apple") # insert apple after mango
#     ll.print()
#     # # ll.remove_by_value("orange") # remove orange from linked list
#     # ll.print()
#     # ll.remove_by_value("figs")
#     # ll.print()
#     # ll.remove_by_value("grapes")
#     # ll.print()

#     # ll.remove_by_value("mango")
#     # ll.print()

#     # ll.remove_by_value("apple")
#     # ll.print()
#     ll.insertBefore('mango','ibrahim')
#     ll.print()



class Node :
    def __init__(self,current=None,next=None):
        self.current=current
        self.next=next


class LinkedList :
    def __init__(self):
        self.head=None

    def insert_at_beganing(self,current):
        node = Node(current,self.head)
        self.head = node
    def print(self):
        if self.head is None :
            print('ll is empty')
            return

        itr=self.head
        llstr=''
        while itr:
            llstr += str(itr.current) + '--->'
            itr = itr.next
        print(llstr)

    def insert_at_end(self,data):

        if self.head == None :
            self.head = Node(data,None)
            return
        while self.head.next :
            self.head=self.head.next
        self.head.next=Node(data,None)

    def get_length(self):
        count =0
        if self.head == None:
            return 'empty'
        while self.head:
            self.head=self.head.next
            count+=1
        return print(count)

    def remove_at(self,index):
        if not self.head :
            return 'empty'
        count =0
        while self.head:
            self.head=self.head.next
            count+=1
            itr=self.head
            if count == index :
                itr.se

    # def zipLists(self, list1,list2):

    #         list1_curr = list1.head
    #         list2_curr = list2.head
    #         while list1_curr != None and list2_curr != None:
    #             list1_next = list1_curr.next
    #             list2_next = list2_curr.next
    #             list1_curr.next = list2_curr
    #             list2_curr.next = list1_next
    #             list1_curr = list1_next
    #             list2_curr = list2_next
    #             if list1_curr.next == None:
    #                 break
    #         if list1_curr:
    #             list1_curr.next = list2_curr

    #         return list1

    def zipLists(self, list1,list2):
        list1_curent = list1.head
        list2_current=list2.head

        if list1_curent!= None and list2_current!= None :
            list1_next = list1_curent.next
            list2_next = list2_current.next
            list1_curent.next=list2_current
            list2_current.next=list2_next
            list1_curent=list1_next
            list2_current=list2_next



    def insert_after_value(self, data_after, data_to_insert):
        if not self.head :
            return 'empty'
        itr =self.head
        while itr :

            if itr.current == data_after:
                itr.next=Node(data_to_insert,itr.next)
                break
            itr=itr.next

    def insertBefore(self,data_before,data_to_insert):
        if not self.head:
            return 'empty'

        itr=self.head
        while itr :
            if itr.next == data_before :
                itr.current == Node(data_to_insert,itr.next)
                break
            itr=itr.next



    def removeDuplicates(self):
            """
            time O(n)
            space O(1)
            """
            itr = self.head
            if itr == None:
                return
            while itr.next:
                if itr.current == itr.next:
                    itr=itr.next
                    new = itr.next
                    itr.next = new
                    itr=None

                else:
                    itr = itr.next

    def kth_from_end(self,k):
        current=self.head
        length=0
        while current:
            current=current.next
            length+=1
        if k>length :
            print('bigger')
            return"biggrt"
        if k<0:
            print('negative')
            return"negative"

        itr=self.head

        for i in range(0,length-k-1):
            itr=itr.next

        print(itr.current)



if __name__ == "__main__" :
    ll= LinkedList()
    ll.insert_at_end(3)

    ll.insert_at_beganing(8)
    ll.insert_at_beganing(8)
    ll.insert_at_beganing(777)
    ll.removeDuplicates()
    ll.insert_at_beganing(87)
    ll.print()
    # ll.print()
    # ll.get_length()

    # ll.print()











































