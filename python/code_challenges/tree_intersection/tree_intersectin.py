
from python.code_challenges.hashtable.hashtable import HashTable , LinkedList
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



