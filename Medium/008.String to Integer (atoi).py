# 

'''
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.
code[45] = char[-]
code[46] = char[.]
code[47] = char[/]
code[48] = char[0]
code[49] = char[1]
code[50] = char[2]
code[51] = char[3]
code[52] = char[4]
code[53] = char[5]
code[54] = char[6]
code[55] = char[7]
code[56] = char[8]
code[57] = char[9]
'''


class Solution(object):
	# def safeDigital(self, charIn):
	# 	digitalRange = range(48,57 + 1)
	# 	code = ord(charIn)
	# 	digital = 0

	# 	if code in digitalRange:
	# 		digital = code - 48
	# 	else:
	# 		digital = -1

	# 	return digital


	def myAtoi(self, str):
		"""
		:type str: str
		:rtype: int
		"""

		code0 = ord('0')
		code9 = ord('9')
		digitalRange = range(code0, code9 + 1)

		digital = 0
		number = 0

		sign = 1
		cleanStr = str.strip()
		if cleanStr.startswith('-'):
			sign = -1
			cleanStr = cleanStr[1:] 
		elif cleanStr.startswith('+'):
			sign = 1
			cleanStr = cleanStr[1:]

		strLength = len(cleanStr)
		for i in range(strLength):
			# code = ord(cleanStr[-1 * (i+1)])
			code = ord(cleanStr[i])
			power = 10 ** (len(cleanStr) - (i + 1))
			if code in digitalRange:
				digital = code - code0
				number += digital * power
			else:
				number = number / power / 10
				break


 # INT_MAX (2147483647) or INT_MIN (-2147483648) 


		if sign > 0:
			number = min(number, 2147483647)
		else:
			number = max(sign * number, -2147483648)

		return number



   

# class Solution(object):
#     def myAtoi(self, str):
#         """
#         :type str: str
#         :rtype: int
#         """
#         result = 0
#         if len(str):
#             result = int(str)
            
#         return result

        
def test():
	items = [
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
		print '{0} - {1}'.format(item, solution.myAtoi(item))


test()


def check_ascii(items):
	for item in items:
		print 'char[{0}] = code[{1}]'.format(item, ord(item))

def print_ascii(items):
	for item in items:
		print 'code[{0}] = char[{1}]'.format(item, chr(item))

# print chr(97)
check_ascii([
		'0',
		'1',
		'-',
		'+',
	])

print "*"*32
print 2**31

testString = '1234566890'
outString = ''
for i in range(10):
	outString = outString + testString[-1*(i+1)]

print outString
