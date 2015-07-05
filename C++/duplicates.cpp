//This program removes duplicated from an array

#include <iostream>
#include <iomanip>
#include <cstring>

using namespace std;


//Function Prototypes
void checker(int[10]);

int main()
{
    int numbers[10];
    int beginning;

    cout << "Please enter 10 integers, hitting return after each one: \n";

    for(beginning = 0; beginning < 10;beginning++)
    {
        cin >> numbers[beginning];
    }

    checker(numbers);

	return 0;
}

//Definition of the function checker which checks the arrays for duplicates
void checker(int list[10])
{
    int start = 0;
    int shift = 0;

    bool checked[10] = {false,false,false,false,false,false,false,false,false,false};

    for(start = 0;start < 10; start++)
    {
        for(shift = 0;shift < 10;shift++)
            {
                if (list[start] == list[shift])
                    {
                        if (checked[start] == false && checked[shift] == false)
                            {
                                checked[start] = true;
                                checked[shift] = true;
                                cout << list[start] << " ";
                            }
                        else if (checked[start] == true || checked[shift] == true)
                            {
                                checked[start] = true;
                                checked[shift] = true;
                                continue;
                            }
                    }
                else if (list[start] != list[shift])
                    {
                        continue;
                    }
            }
    }
}
