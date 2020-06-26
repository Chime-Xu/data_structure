from typing import Any, Optional

class Node:
    def __init__(self, data: Any, next: Optional = None):
        self.data: Any = data
        self.next: Optional = next

    def __repr__(self):
        return f'Node({self.data})'


class LinkQueue:
    def __init__(self):
        self.front: Optional[Node] = None  # 头结点
        self.rear: Optional[Node] = None  # 尾结点
        self.size = 0

    def put(self, item: Any) -> None:
        node: Node = Node(item)
        if self.is_empty():
            self.front = node  # 只包含一个结点的情况,前后都指向同一个结点
            self.rear = node
        else:
            # assert isinstance(self.rear,node)
            self.rear.next = node
            self.rear = node
        self.size += 1

    def pop(self):  # 出队
        if self.is_empty():
            raise IndexError('Empty Queue')
        else:
            node: Node = self.front
            self.front = node.next
        self.size -= 1
        return node.data

    def is_empty(self) -> bool:
        return self.front is None

    def get(self, index):  # 遍历链表
        if self.is_empty():
            raise IndexError('Empty Queue')
        else:
            curr = self.front
            for i in range(1, index):
                curr = curr.next
            return curr

    def __repr__(self):
        curr = self.front
        str = ''
        while curr:
            str += f'{curr}-->'
            curr = curr.next
        return str + 'END'


if __name__ == '__main__':
    q = LinkQueue()
    # print(q.is_empty())
    q.put(1)
    q.put(2)
    q.put(3)
    print(q)
    q.pop()
    print(q)
    print(q.is_empty())
    print(q.front)
    print(q.size)
    print(q.get(2))
