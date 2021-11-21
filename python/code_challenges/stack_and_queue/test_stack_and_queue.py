
from stack_and_queue.stack_and_queue import Stack
def test_push_pop_peek():
    stack = Stack()
    for i in range(1,11):
        stack.push(i)
    stack.push(10)
    assert stack.top.value == 11
    assert stack.pop() == 10
    assert stack.peek() == 10

def test_is_empty():

    stack =Stack()
    assert stack.is_empty( ) == True
