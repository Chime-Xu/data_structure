from typing import Any,Optional

class Node:
    def __init__(self,data: Any,next: Optional=None):
        self.data: Any=data
        self.next: Optional=next
    def __repr__(self):
        return f'Node({self.data})'
class LinkQueue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.size=0
    def __repr__(self):
        curr=self.front
        str=''
        while curr:
            str += f'{curr}-->'
            curr=curr.next
        return str+'END'
    def is_empty(self):
        return self.front is None
    def put(self, item):
        node=Node(item)
        if self.is_empty():
            self.front=node
            self.rear=node
        else:
            self.rear.next=node
            self.rear=node
        self.size += 1
    def pop(self):
        if self.is_empty():
            raise IndexError('Empty Queue')
        else:
            node=self.front
            self.front=node.next
        self.size -= 1
        return node.data
    def get(self,index):
        if self.is_empty():
            raise IndexError('Empty Queue')
        else:
            curr=self.front
            for i in range(1, index):
                curr=curr.next
            return curr
if __name__ == '__main__':
    q=LinkQueue()
    q.put(1)
    q.put(2)
    q.put(3)
    print(q)
    print(q.get(2))
    q.pop()
    print(q)










