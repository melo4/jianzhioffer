# -*- coding: utf-8 -*-
# @Time    : 2019/3/21 下午7:00
# @Author  : Meng Xiao


def replaceSpace(s):
    # write code here
    if not isinstance(s, str) or len(s) <= 0 or s == None:
        return ''
    spaceNum = 0
    for i in s:
        if i == " ":
            spaceNum += 1

    newStrLen = len(s) + spaceNum * 2
    newStr = newStrLen * [None]
    indexOfOriginal, indexOfNew = len(s) - 1, newStrLen - 1
    while indexOfNew >= 0 and indexOfOriginal <= indexOfNew:
        if s[indexOfOriginal] == ' ':
            newStr[indexOfNew - 2: indexOfNew + 1] = ['%', '2', '0']
            indexOfNew -= 3
            indexOfOriginal -= 1
        else:
            newStr[indexOfNew] = s[indexOfOriginal]
            indexOfNew -= 1
            indexOfOriginal -= 1
    return ''.join(newStr)



print(replaceSpace('we are young'))
