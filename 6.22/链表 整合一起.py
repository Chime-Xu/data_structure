class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def __repr__(self):
        return f'Node({self.data})'
class LinkList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
    def __repr__(self):
        curr=self.head
        str=''
        while curr:
            str=str+f'{curr}--->'
            curr=curr.next
        return str+'END'
    def get(self,index):
        #遍历链表之前先找到链表头
        curr=self.head
        #已知次数,适用于for循环
        for i in range(0,index):  #for i in range(1,index)
            curr=curr.next
        return curr
    def insert(self,index,element):
        new_node = Node(element)
        if index<0 or index>self.size:
            raise Exception('索引越界')
        elif self.size==0: #空链表
            self.head=new_node
            self.tail=new_node
        elif index==0: #头部
            new_node.next=self.head
            self.head=new_node
        elif index==self.size: #尾部
            self.tail.next=new_node
            self.tail=new_node
        else:
            prev=self.get(index-1)
            new_node.next=prev.next #需要注意,把要插入的结点的后继结点做好
            prev.next=new_node
        self.size+=1
    def remove(self, index):
        if index < 0 or index > self.size:
            raise Exception('索引越界')
        elif index==0:  #头部
            remove_node=self.head
            self.head=self.head.next
        elif index==self.size-1:
            prev=self.get(index-1)
            remove_node=prev.next   #标记
            prev.next=None
            self.tail=prev
        else:
            prev=self.get(index-1)
            remove_node=prev.next
            prev.next=prev.next.next
        self.size -= 1
        return remove_node.data
    def reverse(self):
        prev=None
        curr=self.head
        while curr is not None:
            temp=curr.next
            # if prev is None:
            #     curr.next = prev
            # else:
            #     curr.next = prev
            curr.next = prev
            prev=curr
            curr=temp
        self.head=prev

if __name__ == '__main__':
    a=LinkList()
    a.insert(0,1)
    a.insert(1,2)
    a.insert(2,3)
    a.insert(2,4)
    print(a)
    print('--------')
    a.get(2)
    print(a)   #不正确
    print('--------')
    # print('get获取为:{}'.format(a.get(1)))
    print(a.get(2))
    print('--------')
    a.remove(3)
    print(a)
    print('--------')
    a.reverse()
    print(a)

