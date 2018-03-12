# 

'''
https://leetcode.com/problems/palindrome-number/

Determine whether an integer is a palindrome. Do this without extra space.


sign (of < 0, return false)
overflow
is number

'''

class Solution(object):
	def isPalindrome(self, x):
		"""
		:type x: int
		:rtype: bool
		"""

		cleanX = str(x).strip()
		if x >= 0 and x < 2147483647 and cleanX == cleanX[::-1]:
			return True
		else:
			return False


def test():
	items = [
	121,
	'+-2',
	'',
	'30302',
	'76634',
	'15856',
	'66042',
	'66021',
	'87908',
	'52323',
	'11720',
	'9013',
	'70938',
	'45015',
	'5657',
	'-9991',
	'89866',
	'-6290',
	'64945',
	'1486',
	'30113',
	'-2984',
	'31690',
	'59443',
	'-3803',
	'91784',
	'28538',
	'1275',
	'98936',
	'12025',
	'1534236469',
	'+1',
	'1',
	"    010",
	"     +004500",
	' +01',
	"  -0012a42",
	"2147483649",
	"-2147483649",
	]

	solution = Solution()
	for item in items:
		print '{0} - {1}'.format(item, solution.isPalindrome(item))


test()



print "*"*32

print 2**31

# -2147447412
 # 2147483648
