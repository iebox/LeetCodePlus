

'''
Given a roman numeral, convert it to an integer.
Input is guaranteed to be within the range from 1 to 3999.


Symbol  I   V   X   L   C   D   M
Value   1   5   10  50  100 500 1,000


  1 :   10 (V X)
I, II, III, IV, V, VI, VII, VIII, IX, X.

 10 :  100 (L C)
X, XX, XXX, XL, L, LX, LXX, LXXX, XC, C.

100 : 1000 (D M)
C, CC, CCC, CD, D, DC, DCC, DCCC, CM, M.

3999 (max)
MMM CM XC IX



1776 as MDCCLXXVI (M DCC LXX VI), the date written on the book held by the Statue of Liberty.[5]
1954 as MCMLIV (M CM L IV), as in the trailer for the movie The Last Time I Saw Paris[6]
1990 as MCMXC, used as the title of musical project Enigma's debut album MCMXC a.D., named after the year of its release.
2014 as MMXIV (MM X IV), the year of the games of the XXII (22nd) Olympic Winter Games (in Sochi)


3999 / 3999 test cases passed.
Status: Accepted
Runtime: 168 ms
Submitted: 0 minutes ago


'''
from functools import reduce

class Solution:

    roman0 = {
        'I': 1,
        'II': 2,
        'III': 3,
        'IV': 4,
        'V': 5,
        'VI': 6,
        'VII': 7,
        'VIII': 8,
        'IX': 9,

        'X': 10,
        'XX': 20,
        'XXX': 30,
        'XL': 40,
        'L': 50,
        'LX': 60,
        'LXX': 70,
        'LXXX': 80,
        'XC': 90,

        'C': 100,
        'CC': 200,
        'CCC': 300,
        'CD': 400,
        'D': 500,
        'DC': 600,
        'DCC': 700,
        'DCCC': 800,
        'CM': 900,

        'M': 1000,
        'MM': 2000,
        'MMM': 3000,
    }

    roman4 = {
        'VIII': 8,
        'LXXX': 80,
        'DCCC': 800,
    }

    roman3 = {
        'III': 3,
        'VII': 7,
        'XXX': 30,
        'LXX': 70,
        'CCC': 300,
        'DCC': 700,
        'MMM': 3000,
    }

    roman2 = {
        'II': 2,
        'IV': 4,
        'VI': 6,
        'IX': 9,

        'XX': 20,
        'XL': 40,
        'LX': 60,
        'XC': 90,

        'CC': 200,
        'CD': 400,
        'DC': 600,
        'CM': 900,

        'MM': 2000,
    }

    roman1 = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    roman_index = {
        0: roman0,
        1: roman1,
        2: roman2,
        3: roman3,
        4: roman4,
    }

    def burn_down(self, s, n):
        roman_dict = Solution.roman_index[n]

        if s[:n] in roman_dict:
            # digitals.append(s[:n])
            return n
        else:
            n -= 1
            s = s[:n]
            return self.burn_down(s, n)

    def work_on(self, s, results):
        if len(s):
            if len(s) < 4:
                n = len(s)
            else:
                n = 4
            split_index = self.burn_down(s[:n], n)
            results.append(s[:split_index])
            s = s[split_index:]
            return self.work_on(s, results)

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        results = []
        self.work_on(s, results)

        number = reduce(lambda x, y: x + y, 
            map(lambda x: self.roman0[x], results)
            )

        return number

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
        number = sl.romanToInt(k)
        print('test', number, k)
        if number == v:
            print('passed')

test()
