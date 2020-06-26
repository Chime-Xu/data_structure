class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def __repr__(self):
        return f'Node({self.data})'
        # return 'Node(%s)'%self.data
        # return 'Node({})'.format(self.data)
# if __name__ == '__main__':
#     print(Node(6))

class LinkList:
    def __init__(self):
        self.head=None
    def __repr__(self):
        curr=self.head
        str=''
        while curr:
            str=str+f'{curr}--->'
            curr=curr.next
        return str+'END'
    def insert_head(self,data):
        new_node=Node(data)
        if self.head:
            new_node.next=self.head
        self.head = new_node
    def insert(self,i,data):
        new_node=Node(data)
        if self.head is None or i==1:
            self.insert_head(data)
        curr=self.head
        prev=curr
        j=1
        while j<i:
            prev = curr
            curr=curr.next
            j+=1
        prev.next=new_node
        new_node.next=curr
    def append(self,data):
        if self.head is None:
            self.insert_head(data)
        curr=self.head
        while curr.next:
            curr=curr.next
        curr.next=Node(data)
if __name__ == '__main__':
    a=LinkList()
    a.insert_head(5)
    a.insert_head(4)
    a.insert_head(2)
    print(a)
    print('------')
    a.insert(2,3)
    print(a)
    print('------')
    a.append(6)
    print(a)