# https://leetcode.com/problems/zigzag-conversion/


# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string text, int nRows);
# convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".



# Your runtime beats 35.82% of python submissions.




class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        

        # step 1 devide string as 

        # n = 4 , groupMember = 6
		# P  	A   	H   	N
		# A  P	L  S 	I   I 	G
		# A P	L S 	I I 	G
		# Y  	I       R   	


        # n = 3 , groupMember = 4
		# P  	A   	H   	N
		# A P	L S 	I I 	G
		# Y  	I   	R   	


        # n = 2, groupMember = 2
		# P A C A H   	N
		# A B B	L S 	I I 	G



        
def test():
	testStrings = [
	"PAYPALISHIRING",
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
		print solution.convert(string, 3)


test()

