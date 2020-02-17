from Queue import Queue
from TestEngine import TestEngine


def toStringTest():
    try:
        queue = Queue()
        queue.enqueue(1).enqueue(2).enqueue(3)
        testPass = queue.toString() == "[3, 2, 1]"
    except:
        testPass = False
    finally:
        return testPass


def toArrayTest():
    try:
        queue = Queue()
        queue.enqueue(1).enqueue(2).enqueue(3)
        testPass = queue.toArray() == [3, 2, 1]
    except:
        testPass = False
    finally:
        return testPass


def isEmptyTest():
    try:
        queue = Queue()
        queue.enqueue(1).enqueue(2).enqueue(3)
        queue.dequeue()
        queue.dequeue()
        queue.dequeue()
        testPass = queue.isEmpty() == True
    except:
        testPass = False
    finally:
        return testPass


def queueTest():
    try:
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        testPass = queue.toString() == "[2, 1]"
    except:
        testPass = False
    finally:
        return testPass


def queueChainTest():
    try:
        queue = Queue()
        queue.enqueue(1).enqueue(2).enqueue(3).enqueue(4)
        testPass = queue.toString() == "[4, 3, 2, 1]"
    except:
        testPass = False
    finally:
        return testPass


def multipleQueueTest():
    try:
        queue = Queue()
        queue.enqueue(1, 2, 3)
        testPass = queue.toString() == "[3, 2, 1]"
    except:
        testPass = False
    finally:
        return testPass


def peekTest1():
    try:
        queue = Queue()
        testPass = queue.peek() == None
    except:
        testPass = False
    finally:
        return testPass


def peekTest2():
    try:
        queue = Queue()
        queue.enqueue(2)
        testPass = queue.peek() == 2
    except:
        testPass = False
    finally:
        return testPass


def sizeTest():
    try:
        queue = Queue()
        queue.enqueue(2)
        testPass = queue.sizeOf() == 1
    except:
        testPass = False
    finally:
        return testPass


def getTests():
    return [toStringTest, toArrayTest, multipleQueueTest, queueTest,
            queueChainTest, isEmptyTest, peekTest1, peekTest2, sizeTest]


def main():
    testEngine = TestEngine("Queue", getTests())
    testEngine.runTests()


main()
