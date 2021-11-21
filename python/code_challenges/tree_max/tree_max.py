class Node():
    def __init__(self, value=None):

        self.value = value
        self.left = None
        self.right = None

class binary_tree():

    def __init__(self):
        self.root = None

    def pre_order(self ,root):
        pre_order_elemnts =[]
        if root:
            pre_order_elemnts.append(root.value)

            pre_order_elemnts = pre_order_elemnts + self.pre_order(root.left)

            pre_order_elemnts = pre_order_elemnts + self.pre_order(root.right)

        return pre_order_elemnts

    def in_order(self,root):

        in_order_elements=[]
        if root:
            in_order_elements = self.in_order(root.left)

            in_order_elements.append(root.value)
            in_order_elements = in_order_elements + self.in_order(root.right)
        return in_order_elements

    def post_order(self, root):
        post_order_elements=[]
        if root:
            post_order_elements = self.post_order(root.left)
            post_order_elements = post_order_elements + self.post_order(root.right)
            post_order_elements.append(root.value)
        return post_order_elements

    def find_max(self):
        if self.root == None:
          return False
        max = self.root.value
        def max_fun(root):
          nonlocal max

          if root.left:
              max_fun(root.left)
          if root.right:
              max_fun(root.right)
          if root.value > max:
              max = root.value

          return max
        return max_fun(self.root)


class binary_search_tree(binary_tree):

    def add(self, value):
        node = Node(value)
        if value == self.root:
            return

        if self.root == None:
            self.root = node
            return

        current = self.root
        while current:
            if current.value > value:
                if current.right:
                    current = current.right
                else:
                    current.right = node
                    return
            if current.value < value:
                if current.left:
                   current = current.left
                else:
                    current.left = node
                    return

    def contains(self, value):
        if value == self.root:
            return True

        current = self.root

        while current:
            if current.value > value:
                if current.right:
                   current = current.right
                else:
                    return False
            if current.value < value:
                if current.left:
                   current = current.left
                else:
                    return False
            if current.value == value:
                return True
        return False

if __name__=="__main__":

    binarytree = binary_tree()
    binarytree.root = Node(1)
    binarytree.root.left = Node(2)
    binarytree.root.left.left = Node(333)
    print("Max:",binarytree.find_max())



    pass

