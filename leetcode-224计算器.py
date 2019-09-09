# -*- coding: utf-8 -*-
# @Time    : 2019/8/31 17:13
# @Author  : Meng Xiao

# 计算单独的表达式
def eval_(S):
    opt_set1 = ('*', '/')
    opt_set2 = ('+', '-')
    st = [S[0]]
    for i in range(1, len(S)):
        if S[i-1] not in opt_set1:
            st.append(S[i])
        else:
            st.pop()
            if S[i-1] == '*':
                d = int(st.pop()) * int(S[i])
            else:
                d = int(st.pop()) / int(S[i])
            st.append(str(int(d)))
    if len(st) == 1:
        return int(st[0])
    res = 0
    for i in range(1, len(st)):
        if st[i-1] not in opt_set2:
            continue
        if st[i-1] == '+':   # 这里不对
            res += int(st[i-2]) + int(st[i])
        else:
            res += int(st[i-2]) - int(st[i])
    return res

def cal(S):  # 先去括号
    st = []
    for s in S:
        if s != ')':
            st.append(s)
        else:
            temp = ''
            tmp = st.pop()
            while tmp != '(':
                temp += tmp
                tmp = st.pop()
            st.append(str(eval_(temp)))

    return eval_(''.join(st))

print(cal("(3-(5-(8)-(2+(9-(0-(8-(2))))-(4))-(4)))"))