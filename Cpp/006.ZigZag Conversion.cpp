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
    string convert(string s, int numRows) {
        string res="";
        if(numRows==1) return s;
        for(int i=0; i < numRows; i++){
            for(int j=0, k=i; k < s.size(); j++){
                res += s[k];
                k += ((i==0 || (j%2==0)) && (i!= numRows-1) )? 2*(numRows-i-1) : 2*i;
            }
        }
        return res;
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
		int result = so.convert(items[i], i);
		cout << items[i] << " - " << result << endl;
	}

	return 0;
}


        
