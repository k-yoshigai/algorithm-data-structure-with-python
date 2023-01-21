from typing import Any


class Queue(object):
    def __init__(self):
        self.queue = []

    def enqueue(self, data: Any) -> None:
        self.queue.append(data)

    def dequeue(self) -> Any:
        if self.queue:
            return self.queue.pop(0)

    def reverse(self) -> None:
        new_queue = []
        while self.queue:
            new_queue.append(self.queue.pop())
        self.queue = new_queue


if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    print(q.queue)

    print(q.dequeue())
    print(q.queue)
    print(q.reverse())
    print(q.queue)
