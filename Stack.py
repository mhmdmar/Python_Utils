class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return self.peek() == None

    def peek(self):
        if len(self.stack) == 0:
            return None
        return self.stack[len(self.stack)-1]

    def pop(self):
        if self.isEmpty() == False:
            return self.stack.pop()

    def sizeOf(self):
        return len(self.stack)

    def push(self, *values):
        for value in values:
            self._push(value)
        return self

    def _push(self, item):
        self.stack.append(item)

    def toArray(self):
        return self.stack[:]  # return new copy of the array

    def toString(self):
        return str(self.stack)
