#include <iostream>
#include <stdio.h>
#include <limits.h>
#include <string>
#include <vector>
using namespace std;

/*
discards all leading whitespaces
sign of the number
overflow
invalid input
*/

class Solution {
public:
	int myAtoi(string str) {
		int sign = 1, base = 0, i = 0;
		while (str[i] == ' ') { i++; }
		if (str[i] == '-' || str[i] == '+') {
			sign = 1 - 2 * (str[i++] == '-'); 
		}
		while (str[i] >= '0' && str[i] <= '9') {
			if (base >  INT_MAX / 10 || (base == INT_MAX / 10 && str[i] - '0' > 7)) {
				if (sign == 1) return INT_MAX;
				else return INT_MIN;
			}
			base  = 10 * base + (str[i++] - '0');
		}
		return base * sign;
	}
};


int main(){
	Solution so;
	const char *itemsArray[] = {
		"",
		"+-2",
		"'"
		"30302",
		"76634",
		"15856",
		"66042",
		"66021",
		"87908",
		"52323",
		"11720",
		"9013",
		"70938",
		"45015",
		"5657",
		"-9991",
		"89866",
		"-6290",
		"64945",
		"1486",
		"30113",
		"-2984",
		"31690",
		"59443",
		"-3803",
		"91784",
		"28538",
		"1275",
		"98936",
		"12025",
		"1534236469",
		"+1",
		"1",
		"    010",
		"     +004500",
		" +01",
		"  -0012a42",
		"2147483649",
		"-2147483649",
	};

	vector<string> items(itemsArray, end(itemsArray));

	for (int i = 0; i < items.size(); i++) {
		int result = so.myAtoi(items[i]);
		cout << items[i] << " - " << result << endl;
	}
}


        
