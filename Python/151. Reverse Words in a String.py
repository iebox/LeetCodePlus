"""

151. Reverse Words in a String
https://leetcode.com/problems/reverse-words-in-a-string/description/


Given an input string, reverse the string word by word.

**Example:**  

```
Input: "the sky is blue",
Output: "blue is sky the".
```

**Note:**

- A word is defined as a sequence of non-space characters.
- Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
- You need to reduce multiple spaces between two words to a single space in the reversed string.

**Follow up:** For C programmers, try to solve it *in-place* in *O*(1) space.


You are here! 
Your runtime beats 36.99 % of python submissions.


"""


import re

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = re.sub(r'[ ]+', ' ', s).strip()
        words = s[::-1].split(' ')
        rwords = map(lambda x: x[::-1], words)

        return ' '.join(rwords)
        


s = Solution()
result = s.reverseWords('the    sky is blue')
print(result)
