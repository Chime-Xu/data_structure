class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def __repr__(self):
        return 'Node({})'.format(self.data)
class LinkList:
    def __init__(self):
        self.head=None
    def __repr__(self):
        curr=self.head
        str=''
        while curr:
            str=str+f'{curr}-->'
            curr=curr.next
        return str+"END"
    def linklist(self,obj):
        self.head=Node(obj[0])
        curr=self.head
        for i in obj[1:]:
            curr.next=Node(i)
            curr=curr.next
    def delete_head(self):
        if self.head is None:
            print('空链表')
        self.head=self.head.next
    def pop(self):
        if self.head is None:
            print('空链表')
        curr=self.head
        while curr.next.next:
            curr=curr.next
        curr.next=None
    def delete_tail(self):
        if self.head is None:
            print('空链表')
        prev=self.head
        curr=prev.next
        while curr.next:
            prev=curr
            curr=curr.next
        prev.next=None
if __name__ == '__main__':
    a=LinkList()
    a.linklist([1,2,3,4])
    print(a)
    print('---------')
    a.delete_head()
    print(a)
    print('---------')
    # a.pop()
    a.delete_tail()
    print(a)


