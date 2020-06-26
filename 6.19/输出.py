class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def __repr__(self):
        return f"Node({self.data})"
class LinkList:
    def __init__(self):
        self.head=None
    def __repr__(self):
        curr=self.head
        str=''
        while curr:
            str=str+f'{curr}-->'
            curr=curr.next
        return str+'END'
    def print_list(self):
        curr=self.head
        while curr:
            print(curr)
            curr=curr.next
    def linklist(self,obj):
        self.head=Node(obj[0])
        curr=self.head
        for i in obj[1:]:
            curr.next=Node(i)
            curr=curr.next
if __name__ == '__main__':
    a=LinkList()
    a.linklist([1,2,3,4])
    print(a)
    a.print_list()