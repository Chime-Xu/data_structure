from typing import List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return 'Node({})'.format(self.data)
        # return f"Node({self.data})"
        # return 'Node(%s)'%self.data

# if __name__ == '__main__':
#     print(Node(6))


class LinkList:
    def __init__(self):
        self.head = None

    # 打印所有结点
    def __repr__(self):
        curr=self.head
        str=''
        while curr:
            str+=f'{curr}-->'
            curr=curr.next
        return str+"END"

    #打印单个值
    def print_list(self):
        curr=self.head
        while curr:
            print(curr.data)
            curr=curr.next

    # 直接列表构建链表
    def linklist(self,obj: List):
        self.head=Node(obj[0])
        curr=self.head
        for i in obj[1:]:
            curr.next=Node(i)
            curr=curr.next

    # 头部插入
    def insert_head(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
        self.head = new_node

    # 尾部插入
    def append(self, data):
        curr = self.head
        if curr is None:
            self.insert_head(data)
        else:
            while curr.next:
                curr = curr.next
            curr.next = Node(data)

    # 中间插入
    def insert(self, i, data):
        new_node = Node(data)
        if self.head is None or i == 1:
            self.insert_head(data)
        else:
            curr = self.head
            prev = curr
            j = 1
            while j < i:
                prev = curr
                curr = curr.next
                j += 1
            prev.next = new_node
            new_node.next = curr

    # 删除头部
    def delete_head(self):
        if self.head is None:
            print("空链表")
        else:
            self.head = self.head.next

    # 删除尾部---1
    def pop(self):
        if self.head is None:
            print("空链表")
        else:
            curr = self.head
            while curr.next.next is not None:
                curr = curr.next
            curr.next = None

    # 删除尾部---2
    def delete_tail(self):
        if self.head is None:
            print("空链表")
        else:
            prev = self.head
            curr = prev.next
            while curr.next:
                prev = curr
                curr = curr.next
            prev.next = None
if __name__ == '__main__':
    a = LinkList()
    a.insert_head(4)
    a.insert_head(3)
    a.append(2)
    a.insert(2, 2)
    print(a)
    # a.print_list()
    print('-----------')
    a.delete_head()
    # a.pop()
    a.delete_tail()
    print(a)
    print('-----------')
    a.linklist([1,2,3,4])
    print(a)
