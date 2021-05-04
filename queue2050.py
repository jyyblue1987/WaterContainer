import unittest

class Queue:
    """ a custom queue implementation using a python list """

    def __init__(self):
        """ instantiate the single field/attribute of our queue object """
        self.queueList = []

    def __str__(self):
        """ override str function so that our queue prints nicely """
        if len(self.queueList) <= 10:
            return "Field 'queueList' = " + str(self.queueList)
        else:
            return "Field 'queueList' = " + str(self.queueList[0:5]) + \
        '[,...]' + str(self.queueList[-5:])

    def isEmpty(self):
        """ return True if the queue is empty, False otherwise """
        return self.queueList == []

    def enqueue(self, new_item):
        """ add a new item to the back (left) of the queue """
        self.queueList.insert(0, new_item)

    def dequeue(self):
        """ remove and return the item at the front (right) of the queue """
        return self.queueList.pop()

    def peek(self):
        """ return item (but don't remove it) from front """
        return self.queueList[-1]

    def size(self):
        """ return the number of items in the queue """
        return len(self.queueList)

class TestQueue(unittest.TestCase):

    def testEnqueue(self):
        q = Queue()
        # ADD LINES NEEDED HERE FOR THIS TEST TO PASS
        self.assertIn("[5, 8]", str(q))

    def testDequeue(self):
        q = Queue()
        # ADD LINE(S) NEEDED HERE FOR THIS TEST TO PASS
        dequeued_item = q.dequeue()
        self.assertEqual(dequeued_item, 7)

if __name__ == '__main__':
    unittest.main()
