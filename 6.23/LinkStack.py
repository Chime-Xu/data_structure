# 导入typing包,用作类型注解
from typing import Any, Optional, NoReturn


class Node:
    def __init__(self, data: Any, next: Optional = None):  # next 为可选类型,可为Node
        self.data: Any = data
        self.next: Optional[Node] = next

    def __repr__(self):  # string representation of a Node
        return f'Node({self.data})'  # 字符串格式化


class LinkStack:
    def __init__(self) -> NoReturn:
        self.top: Optional[Node] = None
        self.size=0

    def __repr__(self):  # 栈用链表表示出来
        curr = self.top
        str = ''
        while curr:
            str += f'{curr}-->'
            curr = curr.next
        return str + 'END'

    def push(self, item: Any) -> None:
        newnode: Node = Node(item)
        if self.top is None:
            self.top = newnode
        else:
            newnode.next = self.top
            self.top = newnode
        self.size +=1

    def pop(self) -> Any:
        if self.top is None:
            raise IndexError('pop from an empty stack')
        else:
            node: Node = self.top
            self.top = node.next
            self.size -= 1
            return node.data

    def is_empty(self) -> bool:
        return self.top is None

    def capacity(self):
        return self.size

if __name__ == '__main__':
    s = LinkStack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push('data_structure')
    print(s)
    # print(s.size)
    print(s.capacity())
    s.pop()
    print(s)
    print(s.is_empty())
    print(s.size)
