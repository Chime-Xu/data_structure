class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def __repr__(self):
        return f'Node({self.data})'
class LinkStack:
    def __init__(self):
        self.top=None
    def __repr__(self):
        curr=self.top
        str=''
        while curr:
            str += f'{curr}-->'
            curr=curr.next
        return str+'END'
    def push(self,element):
        newnode=Node(element)
        if self.top is None:
            self.top=newnode
        else:
            newnode.next=self.top
            self.top=newnode
    def pop(self):
        if self.top is None:
            raise IndexError('空栈')
        else:
            temp=self.top
            self.top=temp.next
    def is_empty(self):
        return self.top is None

if __name__ == '__main__':
    a=LinkStack()
    a.push(1)
    a.push(2)
    a.push(3)
    a.push(4)
    print(a)
    a.pop()
    print(a)
    print(a.is_empty())


