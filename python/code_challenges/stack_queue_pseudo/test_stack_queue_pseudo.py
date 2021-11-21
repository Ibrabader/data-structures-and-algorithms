from stack_queue_pseudo.stack_queue_pseudo import PseudoQueue

def test_PseudoQueue():

    queue_test = PseudoQueue()

    queue_test.enqueue(5)
    queue_test.enqueue(7)
    queue_test.enqueue('ll')

    assert queue_test.dequeue() == 5
    assert queue_test.dequeue() == 7
    assert queue_test.dequeue() == '11'

#  unable to test the units !
