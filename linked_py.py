class Node:
    def __init__(self, value: int) -> None:
        self.data = value
        self.next: Node | None = None
        self.prev: Node | None = None


class PyIterator:
    def __init__(self, head: Node | None):
        self.ptr = head

    def __iter__(self):
        return self

    def __next__(self):
        if self.ptr is None:
            raise StopIteration

        value = self.ptr.data
        self.ptr = self.ptr.next

        return value


class PyLinkedList:
    def __init__(self):
        self.head: Node | None = None
        self.back: Node | None = None
        self.lenght = 0

    def insert(self, index: int, value: int):
        if index < 0 or index > self.lenght:
            return

        if self.lenght == 0:
            self.init(value)
            return

        if index == 0:
            self.pushHead(value)
            return

        if index == self.lenght:
            self.pushBack(value)
            return

        node = self.head
        for _ in range(1, index):
            node = node.next

        new = Node(value)
        new.next = node.next
        new.prev = node
        if node.next is not None:
            node.next.prev = new
        node.next = new

        self.lenght += 1

    def init(self, value: int):
        self.head = Node(value)
        self.back = self.head
        self.lenght = 1

    def pushHead(self, value: int):
        if self.lenght == 0:
            self.init(value)
            return

        new = Node(value)
        new.next = self.head
        self.head.prev = new
        self.head = new

        self.lenght += 1

    def pushBack(self, value: int):
        if self.lenght == 0:
            self.init(value)
            return

        new = Node(value)
        self.back.next = new
        new.prev = self.back
        self.back = new

        self.lenght += 1

    def pop(self, index: int):
        if index < 0 or index >= self.lenght:
            return

        if self.lenght == 0:
            return

        if index == 0:
            self.popHead()
            return

        if index == self.lenght - 1:
            self.popBack()
            return

        node = self.head
        for _ in range(1, index + 1):
            node = node.next

        node.prev.next = node.next
        node.next.prev = node.prev

        self.lenght -= 1

    def popHead(self):
        if self.lenght == 0:
            return

        if self.lenght == 1:
            self.head = None
            self.back = None
            self.lenght = 0
            return

        self.head = self.head.next
        self.head.prev = None
        self.lenght -= 1

    def popBack(self):
        if self.lenght == 0:
            return

        if self.lenght == 1:
            self.head = None
            self.back = None
            self.lenght = 0
            return

        self.back = self.back.prev
        self.back.next = None
        self.lenght -= 1

    def __len__(self):
        return self.lenght

    def iter(self):
        return PyIterator(self.head)
