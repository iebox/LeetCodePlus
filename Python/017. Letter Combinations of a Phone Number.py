"""

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


==============
2    abc
3    def
4    ghi
5    jkl
6    mno
7    pqrs
8    tuv
9    wxyz


Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.



============

Submission Detail
25 / 25 test cases passed.
Status: Accepted
Runtime: 36 ms
Submitted: 0 minutes ago
Accepted Solutions Runtime Distribution

05101520253035404550556065700102030405060
python3
You are here! 
Your runtime beats 90.09 % of python3 submissions


"""

class Solution:
    def merge(self, ready_combos, rest_combos):
        if len(rest_combos):
            todo_letters = [letter for letter in rest_combos[0]]
            print(todo_letters)

            # new_ready = list(map(lambda x, y: x + y, todo_letters, ready_combos))

            new_ready_combos = []

            for r in todo_letters:
            	new_ready = list(map(lambda x: x + r, ready_combos))
            	new_ready_combos.extend(new_ready)

            return self.merge(new_ready_combos, rest_combos[1:])
        else:
            return ready_combos

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
        	return []
        map_dict = {
            2: 'abc',
            3: 'def',
            4: 'ghi',
            5: 'jkl',
            6: 'mno',
            7: 'pqrs',
            8: 'tuv',
            9: 'wxyz',
        }

        combos = [map_dict[int(digit)] for digit in digits]

        # print(combos)

        results = self.merge([''], combos)
        # print(results)
        return results


s = Solution()

r = s.letterCombinations('234')
print(r)

r = s.letterCombinations('')
print(r)

