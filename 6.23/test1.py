class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f'Node({self.data})'

class LinkStack:
    def __init__(self):
        self.top=None

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
            return temp.data
    def is_empty(self):
        return self.top is None

    def __repr__(self):
        curr=self.top
        str=''
        while curr:
            str=str+f'{curr}-->'
            curr=curr.next
        return str+"END"

if __name__ == '__main__':
    l=LinkStack()
    print(l.is_empty())
    l.push(1)
    l.push(2)
    l.push(3)
    print(l)
    l.pop()
    print(l)
    print(l.pop())





