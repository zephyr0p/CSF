#include <bits/stdc++.h>
using namespace std;

// Returns true if given two strings are same
bool checkCaptcha(string& captcha, string& user_captcha)
{
	return captcha.compare(user_captcha) == 0;
}

// Generates a CAPTCHA of given length
string generateCaptcha(int n)
{
	time_t t;
	srand((unsigned)time(&t));

	// Characters to be included
	char* chrs = "abcdefghijklmnopqrstuvwxyzABCDEFGHI"
				"JKLMNOPQRSTUVWXYZ0123456789";

	// Generate n characters from above set and
	// add these characters to captcha.
	string captcha = "";
	while (n--)
		captcha.push_back(chrs[rand() % 62]);

	return captcha;
}

// Driver code
int main()
{
	// Generate a random CAPTCHA
	string captcha = generateCaptcha(9);
	cout << captcha;

	// Ask user to enter a CAPTCHA
	string usr_captcha;
	cout << "\nEnter above CAPTCHA: ";
	cin >> usr_captcha;

	// Notify user about matching status
	if (checkCaptcha(captcha, usr_captcha))
		printf("\nCAPTCHA Matched");
	else
		printf("\nCAPTCHA Not Matched");

	return 0;
}
