# -*- coding: utf-8 -*-
# @Time    : 2019/4/1 下午8:01
# @Author  : Meng Xiao
class Solution:
    def match(self, s, pattern):
        if len(s) == 0 and len(pattern) == 0:
            return True
        elif len(s) != 0 and len(pattern) == 0:
            return False
        elif len(s) == 0 and len(pattern) != 0:
            if len(pattern) > 1 and pattern[1] == '*':
                return self.match(s, pattern[2:])
            else:
                return False

        # 下面讨论s与pattern 都不为空的情况
        else:
            if len(pattern) > 1 and pattern[1] == '*':
                if s[0] != pattern[0] and pattern[0] != '.':
                    return self.match(s, pattern[2:])

                else:
                    # 如果s[0]与pattern[0]相同，且pattern[1]为*，这个时候有三种情况
                    # pattern后移2个，s不变；相当于把pattern前两位当成空，匹配后面的
                    # pattern后移2个，s后移1个；相当于pattern前两位与s[0]匹配
                    # pattern不变，s后移1个；相当于pattern前两位，与s中的多位进行匹配，因为*可以匹配多位
                    return self.match(s, pattern[2:]) or self.match(s[1:], pattern[2:]) or self.match(s[1:],pattern)

            # pattern第二个字符不为*的情况
            else:
                if s[0] == pattern[0] or pattern[0] == '.':
                    return self.match(s[1:], pattern[1:])
                else:
                    return False
