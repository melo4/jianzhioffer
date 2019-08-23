class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def head_tail(self, head):

        if not head or not head.next:
            return head
        # 找中间结点
        mid = head
        right = head.next
        while right.next and right.next.next:
            mid = mid.next
            right = right.next.next
        right = mid.next
        mid.next = None

        right = self.reverse_list(right) # 链表反转

        # left和right依次相连
        cur = head
        while cur.next:
            tmp = cur.next
            cur.next = right
            right = right.next
            cur.next.next = tmp
            cur = tmp
        cur.next = right

        return head

    def reverse_list(self, head): # 就地逆
        if not head or not head.next:
            return head
        prev = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev

def print_list(head):
    if head == None:
        return
    while head:
        print(head.val, end=' ')
        head = head.next
    print()

# 测试：

if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)
    f = ListNode(6)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    s = Solution()
    print_list(a)
    dummy = s.head_tail(a)
    print_list(dummy)

