# 写一个函数,返回数组中每一个元素除以（/）第一个元素的结果.要求空间复杂度为O(1)  (不能借助空列表)
def shuchu(e):
    for i in range(len(e)-1,-1,-1):
        e[i]/=e[0]
    return e
# e = list(input("输入数组: "))
e = [2, 12, 6, 8, 10]
print(shuchu(e))

