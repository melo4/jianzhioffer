# 线段
def func(num_list):
    start = 1000
    end = 0
    for one_list in num_list:
        if one_list[0] < start:
            start = one_list[0]
        if one_list[1] > end:
            end = one_list[1]
    print(start, end)

    flag = [False] * end
    for i in range(len(num_list)):
        for j in range(num_list[i][0], num_list[i][1]):
            flag[j] = True
    print(flag)
    return flag.count(True)

# n_list = [[1,3],[2,7],[9,11],[13,20],[15,30]]
# print(func(n_list))

# 最大不重复子串
def LongestSubStr(s):
    if not s or len(s) < 2:
        return s
    pindex = [-1] * 26
    curLength = 0
    maxLength = 0
    for i in range(len(s)):
        preIndex = pindex[ord(s[i])-ord('a')]
        if preIndex < 0 or i - preIndex > curLength:
            curLength += 1
        else:
            if curLength > maxLength:
                maxLength = curLength
            curLength = i - preIndex
        pindex[ord(s[i]) - ord('a')] = i
    return maxLength
print(LongestSubStr('arabcacfr'))