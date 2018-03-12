#include <iostream>
#include <stdio.h>
#include <limits.h>
#include <string>
#include <vector>
using namespace std;

/*
https://leetcode.com/problems/palindrome-number/

Determine whether an integer is a palindrome. Do this without extra space.


sign (of < 0, return false)
overflow
is number

*/

class Solution {
public:
	bool isPalindrome(int x) {
		if (x < 0 || (((x % 10) == 0) && x)) return false;
		int rev = 0;
		while ( rev < x) {
			rev = rev * 10 + (x % 10);
			x /= 10;
		}
		return (x == rev || (x == rev/10));
	}
};

int main(){
	Solution so;
	const int itemsArray[] = { 1, 2, 3, 4, 101, -100};

	vector<int> items(itemsArray, end(itemsArray));

	for (int i = 0; i < items.size(); i++) {
		int result = so.isPalindrome(items[i]);
		cout << items[i] << " - " << result << endl;
	}
	return 0;
}