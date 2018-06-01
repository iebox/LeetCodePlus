'''
https://leetcode.com/problems/integer-to-roman

[12] Integer to Roman   (File: 12.integer-to-roman.py)


* Medium (43.88%)
* Total Accepted:    101540
* Total Submissions: 231410
* Testcase Example:  '1'

Given an integer, convert it to a roman numeral.


Input is guaranteed to be within the range from 1 to 3999.

3999 / 3999 test cases passed.
Status: Accepted
Runtime: 136 ms
Submitted: 0 minutes ago

'''


class Solution(object):
    roman0 = {
        0: '',
        1: 'I',
        2: 'II',
        3: 'III',
        4: 'IV',
        5: 'V',
        6: 'VI',
        7: 'VII',
        8: 'VIII',
        9: 'IX',

        10: 'X',
        20: 'XX',
        30: 'XXX',
        40: 'XL',
        50: 'L',
        60: 'LX',
        70: 'LXX',
        80: 'LXXX',
        90: 'XC',

        100: 'C',
        200: 'CC',
        300: 'CCC',
        400: 'CD',
        500: 'D',
        600: 'DC',
        700: 'DCC',
        800: 'DCCC',
        900: 'CM',

        1000: 'M',
        2000: 'MM',
        3000: 'MMM',
    }


    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        s_num = str(num)

        roman = ''
        for i in range(1, len(s_num) + 1):
            digital = int(s_num[-1 * i]) * 10 ** (i - 1)
            # print(digital)
            roman = Solution.roman0[digital] + roman
        return roman




def test():
    sl = Solution()

    case_dict = {
        'MDCCLXXVI': 1776,
        'MCMLIV': 1954,
        'MCMXC': 1990,
        'MMXIV': 2014,
        'IV': 4,
    }

    for k, v in case_dict.items():
        r = sl.intToRoman(v)
        print('test', v, r)
        if r == k:
            print('passed')

test()

        