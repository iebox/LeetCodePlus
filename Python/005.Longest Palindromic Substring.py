# https://leetcode.com/problems/longest-palindromic-substring/

# 5. Longest Palindromic Substring My Submissions Question
# Total Accepted: 92681 Total Submissions: 415071 Difficulty: Medium

# Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.


# Your runtime beats 35.82% of python submissions.




class Solution(object):
	"""
	:type s: str
	:rtype: str
	"""
# take 2
	def maxMatch(self, strTry, strKey):
		match = ''
		for i in range(0, len(strTry)):
			# print '%d [%s] %s' % (i, match, spots)
			match += strTry[i]
			if match not in strKey:
				match = match[:-1]
				break
		return match

	def checkDup(self, strTry, strKey):
		longest = ''

		if strTry == strKey:
			return strTry

		for i in range(0, len(strTry)):
			match = self.maxMatch(strTry[i:], strKey)

			if len(match) > len(longest):
				# avoid case as "acxyzca" output ac
				if len(match) == abs(len(strTry) - strTry.index(match) - strKey.index(match)):
					longest = match
		return longest

	def longestPalindrome(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		if len(s) > 0:
			return self.checkDup(s, s[::-1])
		else:
			return s








# take 1 (failed)

	def isPalindromic(self, s):
		palindromicFlag = True

		mid = len(s)/2
		# for i=0,i<mid,i++:
		for i in range(0,mid):

			print s[i] , s[-(i+1)]
			if s[i-1] != s[-i]:
				palindromicFlag = False
				break
			i += 1
		return palindromicFlag



		# longest = ''
		# semiFinal = ''

		# for char in s:
		# 	semiFinal += str(char)
		# 	if semiFinal in semiFinal:
		# 		continue
		# 	else:

		# 	if buff[-1] == str(char):
		# 		buff = buff[:-1]
		# 		semiFinal += str(char)
		# 	else:
		# 		if len(semiFinal) > len(longest):
		# 			longest = semiFinal
		# 			semiFinal = ''

		# if len(semiFinal) > len(longest):
		# 	longest = semiFinal
		# 	semiFinal = ''	
		# return longest










	def longestPalindromeWithSpaceSep(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		longest = ''
		strings = s.split(' ')
		for string in strings:
			if len(string) > len(longest):
				if self.isPalindromic(string):
					longest = string

		return longest





def test():
	testStrings = [
	"esbtzjaaijqkgmtaajpsdfiqtvxsgfvijpxrvxgfumsuprzlyvhclgkhccmcnquukivlpnjlfteljvykbddtrpmxzcrdqinsnlsteonhcegtkoszzonkwjevlasgjlcquzuhdmmkhfniozhuphcfkeobturbuoefhmtgcvhlsezvkpgfebbdbhiuwdcftenihseorykdguoqotqyscwymtjejpdzqepjkadtftzwebxwyuqwyeegwxhroaaymusddwnjkvsvrwwsmolmidoybsotaqufhepinkkxicvzrgbgsarmizugbvtzfxghkhthzpuetufqvigmyhmlsgfaaqmmlblxbqxpluhaawqkdluwfirfngbhdkjjyfsxglsnakskcbsyafqpwmwmoxjwlhjduayqyzmpkmrjhbqyhongfdxmuwaqgjkcpatgbrqdllbzodnrifvhcfvgbixbwywanivsdjnbrgskyifgvksadvgzzzuogzcukskjxbohofdimkmyqypyuexypwnjlrfpbtkqyngvxjcwvngmilgwbpcsseoywetatfjijsbcekaixvqreelnlmdonknmxerjjhvmqiztsgjkijjtcyetuygqgsikxctvpxrqtuhxreidhwcklkkjayvqdzqqapgdqaapefzjfngdvjsiiivnkfimqkkucltgavwlakcfyhnpgmqxgfyjziliyqhugphhjtlllgtlcsibfdktzhcfuallqlonbsgyyvvyarvaxmchtyrtkgekkmhejwvsuumhcfcyncgeqtltfmhtlsfswaqpmwpjwgvksvazhwyrzwhyjjdbphhjcmurdcgtbvpkhbkpirhysrpcrntetacyfvgjivhaxgpqhbjahruuejdmaghoaquhiafjqaionbrjbjksxaezosxqmncejjptcksnoq"
	# "ababa",
	# "aaa",
	# "abba",
	# "aa bb aba",
	# "aa bccb aba",
	# "a",
	"",
	# # "ab",
	# "aa",
	# "abb",
	# "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
	]


	solution = Solution()
	for string in testStrings:
		# print string
		results = solution.longestPalindrome(string)
		print results

		# matched = 'yvvy'
		# print string.index(matched) + len(matched)
		# print len(string)-string[::-1].index(matched) 



		



test()

"""
thinking

## with space separated string.

1. write a helper function for Palindromic check
2. go over the list and save the longest

## no space separated string:
string = 'cd1aa1ab'

==== take one ====
1. make a buffer holding all strings
2. pushd into the buffer one by one :
	(buffer = cdd1a)
3. if new element is equal to current top, pop out to semiFinal 
	(buffer = cdd1a a) semiFinal = a
	(buffer = cdd1 1) semiFinal = a1
4. if new element is not equal to current top, update the semiFinal
	(buffer = cdd a) semiFinal = a1 , compare semiFinal with Final
5. mirror the final

failed, too many cases couldn't cover, like: ababa aaaa, etc

===== take two =====
1. reverse string
2. find dup string
3. compare and find the longest


"""