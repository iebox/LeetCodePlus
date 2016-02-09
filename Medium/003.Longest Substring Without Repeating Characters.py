# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# 3. Longest Substring Without Repeating Characters My Submissions Question
# Total Accepted: 124919 Total Submissions: 583636 Difficulty: Medium


# Given a string, find the length of the longest substring without repeating characters. For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.



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