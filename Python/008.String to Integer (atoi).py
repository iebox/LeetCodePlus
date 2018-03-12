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

>>> chr(65)
'A'
>>> ord('a')
97

'''


class Solution0(object):
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
			# sign = 1
			cleanStr = cleanStr[1:]

		strLength = len(cleanStr)
		for i in range(strLength):
			# code = ord(cleanStr[-1 * (i+1)])
			power = 10 ** (len(cleanStr) - (i + 1))

			code = ord(cleanStr[i])
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

# _/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/ 
#  
# _/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/

class Solution1(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if not str:
            return 0
        str=str.strip()
        sign=1
        i=0
        result=0
        if str[0]=='-':
            sign=-1
            i=1
        if str[0]=='+':
            i=1
        for j in range(i, len(str)):
            if not self.isNumerical(str[j]):
                if sign>0:
                    return min(result,2147483647)
                else:
                    return max(-result,-2147483648)
            result=result*10+int(str[j])
        if sign>0:
            return min(result,2**31-1)
        else:
            return max(-result,-2**31)
            
    def isNumerical(self,a):
        if a>='0' and a<='9':
            return True
        else:
            return False


class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        if len(str) == 0:
            return 0
        tmp = "0"
        result = 0
        i = 0
        if str[0] in "+-":
            tmp = str[0]
            i = 1
            
        
        for i in xrange(i, len(str)):
            if str[i].isdigit():
                tmp += str[i]
            else:
                break
                
        MAX_INT = 2147483647
        MIN_INT = -2147483648
                
        if len(tmp) > 1:
            result = int(tmp)
        if result > MAX_INT:
            return MAX_INT
        elif result < MIN_INT:
            return MIN_INT
        else:
            return result
            


        
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
	'594412341234123412341234123414312423143',
	'-3803',
	'917a84',
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




# Your runtime beats 59.50 % of python submissions.

