from typing import Any, Optional, NoReturn
class Node:
    def __init__(self,data: Any,next: Optional=None):
        self.data=data
        self.next=next
    def __repr__(self):
        return 'Node({})'.format(self.data)

class LinkList:
    def __init__(self):
        self.top=None
    def __repr__(self):
        curr=self.top
        str=''
        while curr:
            str += '%s-->'%curr
            curr=curr.next
        return str+'END'
    def push(self,data):
        newnode=Node(data)
        if self.top is None:
            self.top=newnode
        else:
            newnode.next=self.top
            self.top=newnode
    def pop(self):
        if self.top is None:
            raise IndexError("空栈")
        else:
            temp=self.top
            self.top=temp.next
    def is_empty(self):
        return self.top is None
if __name__ == '__main__':
    a=LinkList()
    # a.pop()
    # print(a)
    a.push(1)
    a.push(2)
    a.push(3)
    print(a)
    a.pop()
    print(a)
    print(a.is_empty())