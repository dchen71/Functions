//This program shows syntax memorization

#include <iostream>

using namespace std;

int main()

{

    int aster;
    char Repeat = 'y';

    while (Repeat != 'n')
    {
        cout << "How many asterisks? ";
        cin >> aster;

        for (int i = 0; i < aster; i++)
        {
            cout << "*";
        }

    cout << endl << "Go again? (y/n): ";
    cin >> Repeat;

    }

    return 0;

}
