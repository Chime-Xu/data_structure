"""判断入环点在哪里
判断环长度"""
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def circle(head):
    curr=head
    prev=head
    while curr and curr.next is not None:
        prev=prev.next
        curr=curr.next.next
        if prev==curr:
            return True
    return False

if __name__ == '__main__':
    a1=Node(1)
    a2=Node(2)
    a3=Node(3)
    a4=Node(4)
    a5=Node(5)
    a1.next=a2
    a2.next=a3
    a3.next=a4
    a4.next=a5
    # a5.next=a3
    print(circle(a1))