from typing import Hashable

from hashtable.hashtable import hashtable
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
        hashed_value = hashtable()
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


    def left_join(first_hash,socund_hash):

        output = []
        for i in first_hash.map:
            if i:
                output.append(i)
        for i in range(len(output)):
            hashed = socund_hash.hash(output[i][0])
            if socund_hash.contains(output[i][0]):
                output[i].append(socund_hash.map[hashed][1])
            else:
                output[i].append("None")
        return output

