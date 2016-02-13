# https://leetcode.com/problems/median-of-two-sorted-arrays/

# 4. Median of Two Sorted Arrays My Submissions Question
# Total Accepted: 82281 Total Submissions: 455314 Difficulty: Hard

# There are two sorted arrays nums1 and nums2 of size m and n respectively. Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).




class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = ''
        if len(s) > 1:
        	
        	candidate = s[0]

	        for char in s[1:]:
	        	if char not in candidate:
	        		candidate += char
	        	else:
	        		if len(candidate) > len(longest):
	        			longest = candidate

	        		candidate = candidate[candidate.index(char)+1:]
	        		candidate += char

				# if 1st round ends
		        if len(candidate) > len(longest):
		        	longest = candidate

        	# print 'can:' + candidate
        	# print 'lon:' + longest
	        # return len(longest)
        # elif len(s) == 1:
        	# return 1
    	else:
    		longest = s
    		# return len(s)

    	return len(longest)




        
def test():
	testStrings = [
	"",
	"au",
	"cdd",
	"jbpnbwwd",
	"dvdf",
	"aab",
	"abb",
	"ab",
	"a",
	"abcabcbb", 
	"",
	"12341",
	"aa",

	]


	solution = Solution()
	for string in testStrings:
		print solution.lengthOfLongestSubstring(string)


test()

"""
thinking

1. get the actual 2 numbers
2. calculate the sum
3. reverse the digit and create the list

"""