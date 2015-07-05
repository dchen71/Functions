//This program calculates monthly bank fees

#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
	double balance;
	int checks;
	const int MONTHLY = 10;                         //The $10 Flat Charge
    int lowFee;
    float monthlyFee, checkFee;

	cout << endl;
	cout << "Enter the following information about your checking account.\n";
	cout << endl;

	cout << "Beginning balance: $\n";
	cin >> balance;

    cout << "Number of checks written: \n";
    cin >> checks;

    if (checks < 20 && checks > 0)
        {
            checkFee = 0.1;
            if (balance < 400)
                lowFee = 15;
            else
                lowFee = 0;

            monthlyFee = MONTHLY + (checkFee * checks);
            monthlyFee += lowFee;

            cout << fixed << showpoint << setprecision(2);
            cout << "The bank fee this month is $" << monthlyFee << endl;

            if (monthlyFee > balance)
                {
                    cout << endl;
                    cout << "The account is now overdrawn.\n";
                }
        }
    else if (checks < 40 && checks >= 20)
        {
            checkFee = 0.08;
            if (balance < 400)
                lowFee = 15;
            else
                lowFee = 0;

            monthlyFee = MONTHLY + (checkFee * checks);
            monthlyFee += lowFee;

            cout << fixed << showpoint << setprecision(2);
            cout << "The bank fee this month is $" << monthlyFee << endl;

            if (monthlyFee > balance)
                {
                    cout << endl;
                    cout << "The account is now overdrawn.\n";
                }
        }
    else if (checks < 60 && checks >= 40)
        {
            checkFee = 0.06;
            if (balance < 400)
                lowFee = 15;
            else
                lowFee = 0;

            monthlyFee = MONTHLY + (checkFee * checks);
            monthlyFee += lowFee;

            cout << fixed << showpoint << setprecision(2);
            cout << "The bank fee this month is $" << monthlyFee << endl;

            if (monthlyFee > balance)
                {
                    cout << endl;
                    cout << "The account is now overdrawn.\n";
                }
        }
    else if (checks >= 60)
        {
            checkFee = 0.04;
            if (balance < 400)
                lowFee = 15;
            else
                lowFee = 0;

            monthlyFee = MONTHLY + (checkFee * checks);
            monthlyFee += lowFee;

            cout << fixed << showpoint << setprecision(2);
            cout << "The bank fee this month is $" << monthlyFee << endl;

            if (monthlyFee > balance)
                {
                    cout << endl;
                    cout << "The account is now overdrawn.\n";
                }
        }
    else if (checks == 0)
        {
            checkFee = 0;
            if (balance < 400)
                lowFee = 15;
            else
                lowFee = 0;

            monthlyFee = MONTHLY + (checkFee * checks);
            monthlyFee += lowFee;

            cout << fixed << showpoint << setprecision(2);
            cout << "The bank fee this month is $" << monthlyFee << endl;

            if (monthlyFee > balance)
                {
                    cout << endl;
                    cout << "The account is now overdrawn.\n";
                }
        }
    else
        {
            cout << "The number of checks written must be greater than zero.\n";
            if (balance < 0)
                cout << endl << "The account is now overdrawn.\n";
        }

	return 0;
}
