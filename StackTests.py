from Stack import Stack
from TestEngine import TestEngine


def toStringTest():
    try:
        stack = Stack()
        stack.push(1).push(2).push(3)
        testPass = stack.toString() == "[1, 2, 3]"
    except:
        testPass = False
    finally:
        return testPass


def toArrayTest():
    testPass = True
    try:
        stack = Stack()
        stack.push(1).push(2).push(3)
        stack.toArray() == [1, 2, 3]
    except:
        testPass = False
    finally:
        return testPass


def isEmptyTest():
    try:
        stack = Stack()
        stack.push(1).push(2).push(3)
        stack.pop()
        stack.pop()
        stack.pop()
        testPass = stack.isEmpty() == True
    except:
        testPass = False
    finally:
        return testPass


def peekTest1():
    try:
        stack = Stack()
        testPass = stack.peek() == None
    except:
        testPass = False
    finally:
        return testPass


def peekTest2():
    try:
        stack = Stack()
        stack.push(2)
        testPass = stack.peek() == 2
    except:
        testPass = False
    finally:
        return testPass


def sizeTest():
    try:
        stack = Stack()
        stack.push(2)
        testPass = stack.sizeOf() == 1
    except:
        testPass = False
    finally:
        return testPass


def getTests():
    return [toStringTest, toArrayTest,
            isEmptyTest, peekTest1, peekTest2, sizeTest]


def main():
    testEngine = TestEngine("Stack", getTests())
    testEngine.runTests()


main()
