class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.size = 0
        self.oldest = 0

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.append(item)
            self.size += 1
        else:
            self.storage[self.oldest] = item
            self.oldest += 1

        if self.oldest == self.capacity:
            self.oldest = 0

    def get(self):
        return self.storage