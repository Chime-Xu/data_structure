from typing import List


class Node:  # 结点类
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):  # 重写方法, repr 某个对象的字符串de代表 默认返回值的实现f'q'q
        return f"Node({self.data})"
        # return 'Node({})'.format(self.data)
        # return 'Node(%s)'%self.data

# if __name__ == '__main__':  #实现
#     n=Node(6)
#     print(n)


class LinkList:  # 链表
    def __init__(self):
        self.head = None

    # 头部插入结点
    def insert_head(self, data):
        new_node = Node(data)  # 创建新结点
        # 如果链表不空
        if self.head is not None:
            new_node.next = self.head
        # 如果链表为空,或者已经构造了新链表
        self.head = new_node  # 头部转移

    # 尾部插入结点
    def append(self, data):
        if self.head is None:
            self.insert_head(data)
        else:
            temp = self.head
            while temp.next:  # 判断下一个是否为空,不为空,就前进一步
                temp = temp.next
            temp.next = Node(data)

    # 中间插入
    def insert(self, i: int, data):  # 未判断i超过链表长度,需要判断
        if self.head is None or i == 1:
            self.insert_head(data)
        else:
            new_node = Node(data)
            curr = self.head
            prev = curr
            # 指针交替向前 方法
            j = 1
            while j < i:
                prev = curr
                curr = curr.next
                j += 1
            prev.next = new_node
            new_node.next = curr

    # 直接列表构建链表
    def linklisk(self, obj: List):  # 类型注解
        new_node = Node(obj[0])
        self.head = new_node
        curr = self.head
        for i in obj[1:]:
            curr.next = Node(i)
            curr = curr.next

    # 删除头部结点
    def delete_head(self):
        if self.head is None:
            print("空链表")
        else:
            self.head = self.head.next

    # 删除尾部结点
    def pop(self):
        curr = self.head
        if self.head is None:
            print("空链表")
        else:
            while curr.next.next is not None:
                curr = curr.next
            curr.next = None

    # 删除尾部结点另一种方法, 指针交替向前  删除
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

    # 删除特定元素

    # 只打印链表的值
    def print_list(self):
        temp = self.head  # 头结点
        while temp:  # 遍历链表 方法
            print(temp.data)
            temp = temp.next

    # 将链表结点串起来打印出来
    def __repr__(self):
        current = self.head
        string_repr = ""
        while current is not None:
            string_repr += f"{current} --> "     # '%s-->'%current  # '{}-->'.format(current)
            current = current.next
        return string_repr + "END"


if __name__ == '__main__':
    a = LinkList()
    a.linklisk([1, 2, 3, 4])  # 先执行,后插入
    a.insert_head(1)
    # a.insert_head(2)
    # a.append(3)
    # print(a)
    # print('---------')
    # a.delete_head()
    a.insert(2, 3)
    print(a)
    # print('---------')
    # # a.print_list()
    # a.pop()
    # print(a)
    print('---------')
    a.delete_tail()
    print(a)
