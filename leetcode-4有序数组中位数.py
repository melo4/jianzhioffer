# -*- coding: utf-8 -*-
# @Time    : 2019/5/5 21:20
# @Author  : Meng Xiao

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        def findKth(A, B, k):
            if len(A) == 0:
                return B[k - 1]
            if len(B) == 0:
                return A[k - 1]
            if k == 1:
                return min(A[0], B[0])
            a = A[k // 2 - 1] if len(A) >= k // 2 else None
            b = B[k // 2 - 1] if len(B) >= k // 2 else None
            if b is None or (a is not None and a < b):
                return findKth(A[k // 2:], B, k - k // 2)
            return findKth(A, B[k // 2:], k - k // 2)  # 因为k/2 不一定等于k-k/2

        n = len(nums2) + len(nums1)
        if n % 2 == 1:
            return findKth(nums1, nums2, n // 2 + 1) / 1.0
        else:
            small = findKth(nums1, nums2, n // 2)
            big = findKth(nums1, nums2, n // 2 + 1)
            return (small + big) / 2.0
