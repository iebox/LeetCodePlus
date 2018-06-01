"""
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

[2,3,4] , the median is 3 

[2,3], the median is (2 + 3) / 2 = 2.5 

Design a data structure that supports the following two operations:

- void addNum(int num) - Add a integer number from the data stream to the data structure.
- double findMedian() - Return the median of all elements so far.

**Example:**

```
addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
```


You are here! 
Your runtime beats 42.41 % of python3 submissions.


"""

import bisect 


class MedianFinder:
    """
          *   *
    1, 7, 9, 10,  100, 1000        append 5
           **
   5 1, 7, 9, 10,  100, 1000       append 10
           *   *
   5 1, 2, 9, 10, 10 100, 1000     append 4

    """

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []
        self.size = 0
        self.odd = False
        self.median = 0

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        # if str(num).isdigit():
        # self.nums.append(num)
        # self.nums = sorted(self.nums)
        bisect.insort(self.nums, num) 
        self.size += 1
        self.odd = not self.odd

        mindex = self.size // 2

        if self.odd:
            self.median = self.nums[mindex]
        else:
            self.median = (self.nums[mindex - 1] + self.nums[mindex]) / 2


    def findMedian(self):
        """
        :rtype: float
        """
        return self.median
        



# Your MedianFinder object will be instantiated and called as such:

obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
obj.addNum(3)
obj.addNum(4)
# obj.addNum(10)
# obj.addNum(10)
# obj.addNum(1)
# obj.addNum(1)
# obj.addNum(1)
param_2 = obj.findMedian()

# ["MedianFinder","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum"]

print(param_2)
# print(obj.nums)
# print(obj.size)
# print(obj.odd)

