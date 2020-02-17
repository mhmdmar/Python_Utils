class Queue:
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return self.queue == []

    def enqueue(self, *items):
        for item in items:
            self._enqueue(item)
        return self

    def _enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.pop()

    def sizeOf(self):
        return len(self.queue)

    def toArray(self):
        return self.queue[::-1]  # return new copy of the array

    def toString(self):
        return str(self.toArray())

    def peek(self):
        if(self.isEmpty()):
            return None
        else:
            return self.queue[0]
