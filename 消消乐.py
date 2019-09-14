# -*- coding: utf-8 -*-
# @Time    : 2019/8/5 19:57
# @Author  : Meng Xiao

# 消消乐升级，只要有相同连续数字，全部消除，如1,2,3,3,3,2,3，返回1,3
def xiaoxiaole(a):
    stack = []
    i = 0
    lena = len(a)
    while(i<lena):
        flag = False
        while(i<lena and len(stack)>0 and stack[-1] == a[i]):
            if i < len(a)-2 and a[i+1] != a[i+2]:
                i += 1
                flag = True
        if(flag):
            stack.pop()
        else:
            stack.append(a[i])
            i += 1

    return stack

if __name__ == "__main__":
    a = [1,4,2,2,3,3,2,4,1]
    s = xiaoxiaole(a)
    print(s)