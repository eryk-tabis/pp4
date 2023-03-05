class Fifo:
    def __init__(self):
        self.queue = []

    def add(self, a):
        self.queue.append(a)

    def pop(self):
        return self.queue.pop(0)
