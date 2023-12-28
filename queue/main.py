class Queue:
    def __init__(self):
        self.queue = []

    def add(self, value):
        self.queue.append(value)

    def remove(self):
        return None if not self.queue else self.queue.pop(0)

if __name__ == '__main__':
    q = Queue()
    q.add(1)
    q.remove()