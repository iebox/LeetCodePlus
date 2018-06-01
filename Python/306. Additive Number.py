"""
Additive number is a string whose digits can form additive sequence.

A valid additive sequence should contain **at least** three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

Given a string containing only digits `'0'-'9'`, write a function to determine if it's an additive number.

**Note:** Numbers in the additive sequence **cannot** have leading zeros, so sequence `1, 2, 03` or `1, 02, 3` is invalid.

**Example 1:**

```
Input: "112358"
Output: true 
Explanation: The digits can form an additive sequence: 1, 1, 2, 3, 5, 8. 
             1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
```

**Example 2:**

```
Input: "199100199"
Output: true 
Explanation: The additive sequence is: 1, 99, 100, 199. 
             1 + 99 = 100, 99 + 100 = 199
```

**Follow up:**
How would you handle overflow for very large input integers?


You are here! 

Your runtime beats 86.36 % of python3 submissions.




"""

CEILING = 2 ** 64 - 1

def check(a, b, s, ints):
    # print(a, b, s, ints)

    ab = a + b
    str_ab = str(ab)

    if s.startswith(str_ab):
        if ab > CEILING:
            print(ab)
            return []
        ints.append(ab)
        a = b
        b = ab
        next_s = s[len(str_ab):]

        ints = check(a, b, next_s, ints)
        # return ints
    # else:

    return ints



def run_check(len_a, len_b, S):
    splits = []

    a = int(S[:len_a])
    b = int(S[len_a:len_a + len_b])

    if a > CEILING or b > CEILING:
        return []

    if len_a != len(str(a)) or len_b != len(str(b)):
        return []

    splits.extend([a, b])
    next_str = S[len(str(a) + str(b)):]

    # print('input', a, b, next_str)

    splits = check(a, b, next_str, splits)

    return splits


class Solution:
    def isAdditiveNumber(self, num):
    # def splitIntoFibonacci(self, S):
        """
        :type num: str
        :rtype: bool
        """
        results = []
        additive = False

        if int(num) >= 0 and len(num) >= 3:
            for i in range(1, len(num) // 2 + 2):
                for j in range(1, len(num) // 2 + 2):
                    splits = run_check(i, j, num)
                    str_results = map(lambda x: str(x), splits)

                    if len(splits) > 2 and len(''.join(str_results)) == len(num):
                        results = splits
                        print(results)
                        additive = True
                        break


        return additive




        
def test():
    """
    5 6 1117
    6 11 17

    1, 2,   35
    2, 3,  5

    """
    testpassStrings = [
        "0",
        "000",
        "561117",
        "1235",
        "11235813",
        "1101111",
        "0123",
        "123456579", 
        "00246",
        "539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511",
        "01123581321345589",
        "01123581321345589",
        "0000",
        "123456579",
        "0112",
        "417420815174208193484163452262453871040871393665402264706273658371675923077949581449611550452755",
    ]
    testStrings = [
    "121474836472147483648"
    ]

    solution = Solution()
    # for s in testpassStrings:
    for s in testStrings:
        cp = solution.isAdditiveNumber(s)
        print('===', s, cp)

    # cp = solution.longestCommonPrefix([])
    # print(cp)

test()
