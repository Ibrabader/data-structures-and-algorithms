class Node():
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


class binary_tree():
    def __init__(self):
        self.root = None

    def pre_order(self, root):
        pre_order_output=[]
        if root:
            pre_order_output.append(root.value)
          
        return pre_order_output



