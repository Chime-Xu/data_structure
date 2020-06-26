#先进后出
class Stack:
    def __init__(self,limit=10):
        self.stack=[]  #列表实现
        self.size=0
    # def __bool__(self):  #判断列表是否为空   系统自带bool判断
    #     return bool(self.stack)
    def __repr__(self):  #变成字符串输出
        return str(self.stack)

    #压栈
    def push(self,data):
        if len(self.stack)<self.size:
            raise Exception('stackoverflow')
        self.stack.append(data)
        self.size+=1
    #弹栈
    def pop(self):
        if self.stack:
            temp=self.stack.pop()
            self.size -= 1
            return temp
        else:
            raise Exception('pop from an empty stack')
    def peek(self): #返回最后一个进入的值
        if self.stack:
            return self.stack[-1]
    def is_empty(self):
        return not bool(self.stack)
    def size(self):
        return self.size

if __name__ == '__main__':
    s=Stack(10)
    for i in range(10):
        s.push(i)
    print(s)
    for i in range(5):
        s.pop()
    print(s)
    print(s.peek())
    print(s.is_empty())
    print(s.size)
