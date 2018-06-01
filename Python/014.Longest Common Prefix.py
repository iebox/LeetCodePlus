"""
https://leetcode.com/problems/longest-common-prefix/description/

Write a function to find the longest common prefix string amongst an array of strings.

take 1
https://leetcode.com/submissions/detail/144877958/

117 / 117 test cases passed.
Status: Accepted
Runtime: 80 ms

Your runtime beats 19.36 % of python3 submissions.



take 2
https://leetcode.com/submissions/detail/144878919/

117 / 117 test cases passed.
Status: Accepted
Runtime: 40 ms

Your runtime beats 100.00 % of python3 submissions
"""


from collections import Counter

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''

        cp = ''

        benchmark = strs[0]
        input_count = len(strs)

        for i in range(1, len(benchmark) + 1)[::-1]:
            candi_cp = benchmark[:i] 

            tries = filter(lambda x: x.startswith(candi_cp), strs)
            if len(list(tries)) == input_count:
                cp = candi_cp
                break

        return cp


class Solution1:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''

        cp = ''

        benchmark = strs[0]
        input_count = len(strs)
        full_length = len(benchmark)

        for i in range(1, full_length + 1)[::-1]:
            tries = map(lambda x: x[:i], strs)
            stat = Counter(tries)
            try_cp = benchmark[:i] 

            # print(i, try_cp, stat, full_length, input_count)

            if stat[try_cp] == input_count:
                cp = try_cp
                break

        return cp



        
def test():
    testStrings = [
    "abcabcbb", 
    "abc",
    "abc",
    "abcd",
    "abc"
    ]

    solution = Solution()
    cp = solution.longestCommonPrefix(testStrings)
    print(cp)

    # cp = solution.longestCommonPrefix([])
    # print(cp)

from timeit import timeit

print(timeit(lambda:test(), number=1))



