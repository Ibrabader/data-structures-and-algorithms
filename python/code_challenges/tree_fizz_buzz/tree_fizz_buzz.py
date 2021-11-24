class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class binary_tree:
    def __init__(self):
        self.root = None
        self.output = []

def fizzBuzz(val):
    if val.data % 15 == 0:
        return'FizzBuzz'
    elif val.data %3 == 0:
        return'Fizz'
    elif val.data % 5 == 0:
        return'Buzz'
    else:
        return str(val.data)

def FizzBuzzTree(node_value):
    if node_value.root is None:
        return 'the tree is empty'
    new = binary_tree()
    def traverser(val):
        new.output += [fizzBuzz(val)]
        if val.left:
            traverser(val.left)
        if val.right:
            traverser(val.right)
        return new.output
    return traverser(node_value.root)

if __name__ == "__main__":
    binary_t = binary_tree()
    binary_t.root = Node(20)
    binary_t.root.left = Node(15)
    binary_t.root.right = Node(16)

    expected = ['Buzz', 'FizzBuzz', '16']
    actual=(FizzBuzzTree(binary_t))
    assert actual == expected
    print(FizzBuzzTree(binary_t))
