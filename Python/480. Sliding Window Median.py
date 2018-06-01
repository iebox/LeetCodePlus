"""
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

Examples: 

 

`[2,3,4]` , the median is `3`

`[2,3]`, the median is `(2 + 3) / 2 = 2.5`

Given an array *nums*, there is a sliding window of size *k* which is moving from the very left of the array to the very right. You can only see the *k* numbers in the window. Each time the sliding window moves right by one position. Your job is to output the median array for each window in the original array.

For example,
Given *nums* = `[1,3,-1,-3,5,3,6,7]`, and *k* = 3.

```
Window position                Median
---------------               -----
[1  3  -1] -3  5  3  6  7       1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7       3
 1  3  -1  -3 [5  3  6] 7       5
 1  3  -1  -3  5 [3  6  7]      6
```

Therefore, return the median sliding window as `[1,-1,-1,3,5,6]`.

**Note:** 
You may assume `k` is always valid, ie: `k` is always smaller than input array's size for non-empty array.

You are here! 
Your runtime beats 27.85 % of python3 submissions.

"""

import bisect 


class Solution:
    """
    1,5,2,9,3,0

    1,5,2,   9,    3,0
    """
    def __init__(self):
        self.nums = []

        self.sorted_nums = []

        self.odd = False
        # self.median = 0
        self.mindex = 0

        self.medians = []


    def slide(self, drop, pick):
        self.nums.remove(drop)
        bisect.insort(self.nums, pick) 
        # print(self.nums)

        # if self.odd:

    def get_median(self):
        median = self.nums[self.mindex]

        if not self.odd:
            # 10, 20, median(index = 2, 3rd element), 40
            median = (self.nums[self.mindex - 1] + median) / 2

        self.medians.append(float(median))


    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        self.odd = k % 2
        self.mindex = k // 2

        for i in range(k):
            bisect.insort(self.nums, nums[i])

        self.get_median()

        # for num in nums[k:]:

        for j in range(k, len(nums)):
            to_drop = nums[j - k]
            # print(to_drop)
            self.slide(to_drop, nums[j])
            self.get_median()

        return self.medians



s = Solution()

nums = [1,3,-1,-3,5,3,6,7]
nums = [1,4,2,3,5]
k = 4


results = s.medianSlidingWindow(nums, k)
print(results)