# https://leetcode.com/problems/two-sum/
# Given an array of integers, find two numbers such that they add up to a specific target number.

# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

# You may assume that each input would have exactly one solution.

# Input: numbers={2, 7, 11, 15}, target=9
# Output: index1=1, index2=2
# list = [0,1,2,3]
# print list[4:]

class Solution(object):
    def twoSum(self, nums, target):
    	"""
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums = nums[:]	# keep the input list intact
    	while len(nums):
    		spot = target - nums.pop()
    		if spot in nums:
    			break

    	index1 = nums.index(spot)
    	index2 = len(nums)

    	return [index1 + 1, index2 + 1]

# score
# Your runtime beats 31.77% of python submissions.

# test function
def test(numsTargetPairs):
	sumObject =  Solution()
	for pair in numsTargetPairs:
		nums, target = pair
		results = sumObject.twoSum(nums, target)
		
		print "%d + %d = %d" % (nums[results[0] - 1], nums[results[1] - 1], target) 

# test run
pairs = [
	([1,10,8,13,25,2], 27),
	([0,1,2,0], 0),
	([4,1,2,4,2], 8),
	([3,2,4], 6),
	([1,2,3,4,5], 8),
	([-1,-2,-3,-4,-5], -8), 
]
test(pairs)

