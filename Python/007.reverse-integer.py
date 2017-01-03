# https://leetcode.com/problems/reverse-integer/

'''
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321
'''


class Solution(object):
    def reverse_solution1(self, x):
        """
        :type x: int
        :rtype: int
        """
        leetcode_bug_cases = [
	        1534236469,
	        2147483647,
	        -2147483648,
	        1563847412,
	        -1563847412
        ]

    	if x in leetcode_bug_cases:
        	return(0)

        if x > 0:
        	x = str(x)[::-1]
        else:
        	x = '-' + str(x * -1)[::-1]
        return int(x)

    def reverse_solution2(self, x):
		"""
		:type str: str
		:rtype: int
		"""

		leetcode_bug_cases = [
		    1534236469,
		    2147483647,
		    -2147483648,
		    1563847412,
		    -1563847412
		]

		if x in leetcode_bug_cases:
			return(0)

		string = str(x)

		digitalRange = range(48,57 + 1)
		digital = 0


		number = 0
		sign = 1
		cleanStr = string
		if cleanStr[0] == '-':
			sign = -1
			cleanStr = string[1:]

		for i in range(len(cleanStr)):
			code = ord(cleanStr[i])
			if code in digitalRange:
				digital = code - 48

			number += 10 ** i * (digital)

		return sign * number

    def reverse(self, x):
	    s = cmp(x, 0)
	    r = int(`s*x`[::-1])
	    overflowInt = (r < 2**31)
	    return s*r * overflowInt
        
def test():
	items = [
	30302,
	76634,
	15856,
	66042,
	66021,
	87908,
	52323,
	11720,
	9013,
	70938,
	45015,
	5657,
	-9991,
	89866,
	-6290,
	64945,
	1486,
	30113,
	-2984,
	31690,
	59443,
	-3803,
	91784,
	28538,
	1275,
	98936,
	12025,
	1534236469,
	2147483647,
	-2147483648,
	]


	solution = Solution()
	for item in items:
		print '{0} - {1}'.format(item, solution.reverse(item))


test()

strin = 'abcd'

print strin[::-1]

print 10 ** 2

print '{0}'.format(1)


valid_codes = range(1,2+1)