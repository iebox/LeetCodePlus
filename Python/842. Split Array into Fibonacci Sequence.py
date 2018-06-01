"""
Given a string `S` of digits, such as `S = "123456579"`, we can split it into a *Fibonacci-like sequence* `[123, 456, 579].`

Formally, a Fibonacci-like sequence is a list `F` of non-negative integers such that:

- `0 <= F[i] <= 2^31 - 1`, (that is, each integer fits a 32-bit signed integer type);
- `F.length >= 3`;
- and` F[i] + F[i+1] = F[i+2] `for all `0 <= i < F.length - 2`.

Also, note that when splitting the string into pieces, each piece must not have extra leading zeroes, except if the piece is the number 0 itself.

Return any Fibonacci-like sequence split from `S`, or return `[]` if it cannot be done.

**Example 1:**

```
Input: "123456579"
Output: [123,456,579]
```

**Example 2:**

```
Input: "11235813"
Output: [1,1,2,3,5,8,13]
```

**Example 3:**

```
Input: "112358130"
Output: []
Explanation: The task is impossible.
```

**Example 4:**

```
Input: "0123"
Output: []
Explanation: Leading zeroes are not allowed, so "01", "2", "3" is not valid.
```

**Example 5:**

```
Input: "1101111"
Output: [110, 1, 111]
Explanation: The output [11, 0, 11, 11] would also be accepted.
```

**Note:** 

1. `1 <= S.length <= 200`
2. `S` contains only digits.

"""

CEILING = 2 ** 31 - 1

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
    def splitIntoFibonacci(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        results = []

        if int(S) >= 0:
            for i in range(1, len(S) // 2 + 2):
                for j in range(1, len(S) // 2 + 2):
                    splits = run_check(i, j, S)
                    str_results = map(lambda x: str(x), splits)

                    if len(splits) > 2 and len(''.join(str_results)) == len(S):
                        results = splits
                        break


        return results




        
def test():
    """
    5 6 1117
    6 11 17

    1, 2,   35
    2, 3,  5

    """
    testpassStrings = [
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
    ]

    solution = Solution()
    for s in testpassStrings:
    # for s in testStrings:
        cp = solution.splitIntoFibonacci(s)
        print('===', s, cp)

    # cp = solution.longestCommonPrefix([])
    # print(cp)

test()
