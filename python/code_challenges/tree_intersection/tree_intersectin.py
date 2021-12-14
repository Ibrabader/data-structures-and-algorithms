
from hashtable import HashTable , LinkedList
class Node():
    def __init__(self, value=None):

        self.value = value
        self.left = None
        self.right = None

class binary_tree():

    def __init__(self):
        self.root = None
    def post_order(self, root):
        post_order_elements=[]
        if root:
            post_order_elements = self.post_order(root.left)
            post_order_elements = post_order_elements + self.post_order(root.right)
            post_order_elements.append(root.value)
        return post_order_elements

def tree_intersection(tree1 , tree2):
    tree1 = tree1.post_order(tree1)
    tree2 = tree2.post_order(tree2)
    print(" ' "*4,tree1,tree2," ' "*4)
    hashed_value = HashTable()
    repeat = []
    for node in tree1:
        hashed_value.add(node,node)
    for node in tree2:
        if hashed_value.contains(node):
            repeat.append(node)
        hashed_value.add(node,node)
    if len(repeat)==0:
        return "there is no repeat"

    return repeat




if __name__ == '__main__':

    tree1=binary_tree()
    tree1.root=Node("A")
    tree1.root.left=Node("B")
    tree1.root.right=Node("C")
    tree1.root.left.left=Node("D")
    tree1.root.left.right=Node("E")
    tree1.root.right.left=Node("F")

    tree2=binary_tree()
    tree2.root=Node("A")
    tree2.root.left=Node("B")
    tree2.root.right=Node("k")
    tree2.root.left.left=Node("r")
    tree2.root.left.right=Node("x")
    tree2.root.right.left=Node("m")

    print(tree_intersection(tree1,tree2))
