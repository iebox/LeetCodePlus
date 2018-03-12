# https://leetcode.com/problems/zigzag-conversion/


# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string text, int nRows);
# convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".


# step 1 devide string as 

# n = 4 , groupMember = 6
# P      A    H    N
# A  P    L  S I  I G
# A P    L S  I I  G
# Y      I    R       


# n = 3 , groupMember = 4
# P      A       H       N
# A P    L S     I I     G
# Y      I       R       


# n = 2, groupMember = 2
# P A C A H       N
# A B B    L S     I I     G

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        i = 0
        step = 1

        dictZZ = {}

        if len(s) <= numRows or numRows == 1:
            return s
        for i in range(numRows):
            dictZZ[i] = s[i]

        for oneLetter in s[numRows:]:
	        # print "{0}:{1}".format(i, oneLetter)
	        if i == 0:
	            step = 1
	        elif i == numRows - 1:
	            step = -1
	        i += step

	        dictZZ[i] += oneLetter

        print dictZZ

        return ''.join(dictZZ.values())


        
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
    "ABC",
    ]


    solution = Solution()
    for string in testStrings:
        result = '{0} - {1}'.format(string, solution.convert(string, 2))
        print result
        

    # print solution.convert('abcdefgh', 3)


test()

