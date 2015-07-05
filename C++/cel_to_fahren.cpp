//This program converts centigrade temperatures to fahrenheit temperatures

#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
	double cel, fah;
	const double CONS = (9.0 / 5.0);                         //The 9/5 Constant
    double con;

	cout << "Please enter the centigrade temperature: \n";
	cin >> cel;

    con = CONS * cel;
    fah = con + 32;

    cout << fixed << showpoint << setprecision(1);
	cout << cel;
	cout << " degrees centigrade is equal to ";
	cout << fah;
	cout << " degrees fahrenheit.\n";

	return 0;
}
