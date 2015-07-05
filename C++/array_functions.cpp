//This program has three specific array functions

#include <iostream>
#include <cstdlib>
#include <math.h>

using namespace std;

//Function prototypes
void equalButOpposite();
void averageOfNeighbors();
void allValuesArePaired();
bool palindrome(int first[], int second[], int length);
bool average(float test[], int length);
float averaged(float test[], int position);
bool paired(char test[], int length);

int main()
{

    int selector;

    do
        {
            cout << "Enter 1 for equalButOpposite" << endl;
            cout << "Enter 2 for averageOfNeighbors" << endl;
            cout << "Enter 3 for allValuesArePaired" << endl;
            cin >> selector;

            if (selector == 1)
                equalButOpposite();
            else if (selector == 2)
                averageOfNeighbors();
            else if (selector == 3)
                allValuesArePaired();
            else
                cout << "Please try again" << endl << endl;
        }
    while(selector != 1 || selector != 2 || selector != 3);

    return 0;

}


//Main function to check if equal but opposite
void equalButOpposite()
{
    int length, length1, length2;
    bool answer;
    char restart;

    cout << "Please enter the length:\n";
    cin >> length;

    int number1[length], number2[length];

    cout << "Please enter interger array 1" << endl;
    for (length1 = 0; length1 < length; length1++)
        {
            cout << "Number " << (length1 + 1) << ": ";
            cin >> number1[length1];
        }

    cout << "Please enter interger array 2" << endl;
    for (length2 = 0; length2 < length; length2++)
        {
            cout << "Number " << (length2 + 1) << ": ";
            cin >> number2[length2];
        }

    answer = palindrome(number1, number2, length);

    if (answer == true)
        {
            cout << "The numbers are equal but opposite.\n\n";
        }
    else if (answer == false)
        {
            cout << "The numbers are not equal but opposite.\n\n";
        }

}


//Supports equalButOpposite by actually checking it
bool palindrome(int first[], int second[], int length)
{
    bool answer;
    int start, answerNum;

    for(start = 0; start < length;start++)
        {
            if (first[start] == second[length - 1 - start])
                {
                    answer = true;
                }
            else if (first[start] != second[length - start - 1])
                {
                    answer = false;
                    break;
                }
        }

    return answer;
}

//Main function to check if a average is in either of the neighbors
void averageOfNeighbors()
{
    int length;
    int begin;
    bool answer;

    do
    {
    cout << "Please enter the length:\n";
    cin >> length;

    if (length <= 3)
        {
        cout << "Please input a number greater than 3" << endl;
        begin--;
        }
    else
        continue;

    }
    while (length <= 3);

    float number[length];

    cout << "Please enter numbers" << endl;
    for (begin = 0; begin < length; begin++)
        {
            cout << "Number " << (begin + 1) << ": ";
            cin >> number[begin];
        }

    answer = average(number, length);

    if (answer == true)
        cout << "The numbers are the average of it's neighbors on either side.\n\n";
    else if (answer == false)
        cout << "The numbers are not the average of it's neighbors on either side.\n\n";

    return;
}

//Suuports averageOfNeighbors by telling if it is the average
bool average(float test[], int length)
{
    int start;
    bool answer = false;

    for (start = 1; start < length - 2; start++)
        {
            if (averaged(test, start) == test[start - 1])
                {
                    answer = true;
                    continue;
                }
            else if (averaged(test, start) == test[start + 2])
                {
                    answer = true;
                    continue;
                }
            else if (averaged(test, start) != test[start - 1] && averaged(test, start) != test[start + 2])
                {
                    answer = false;
                    break;
                }
            else if ((start + 1) >= length)
                {
                    break;
                }
        }

    return answer;
}

//Does an average function for the function average
float averaged(float test[], int position)
{
    float average;

    average = (test[position] + test[position + 1])/2;

    return average;
}

//Main function to check if all the values are paired
//Restrictions to element numbers is 1 and odd numbers
void allValuesArePaired()
{
    int length;
    bool answer;
    int start;
    int eval;

    do
    {
        cout << "Please enter the length:\n";
        cin >> length;

        eval = length % 2;

        if(length <= 1)
            cout << "Please enter a value higher than 1" << endl;
        else if (eval == 1)
            cout << "Please enter an even length" << endl;
    }
    while (length <= 1 || (eval == 1));

    char word[length];

    cout << "Please enter characters" << endl;
    for (start = 0; start < length; start++)
        {
            cout << "Character " << (start + 1) << ": ";
            cin >> word[start];
        }

    answer = paired(word, length);

    if (answer == true)
        cout << "The characters are included exactly twice.\n\n";
    else if (answer == false)
        cout << "The characters are not included exactly twice.\n\n";

    return;
}

//Supports allValuesArePaired by telling if values are paired
bool paired(char test[], int length)
{
    int begin, counter;
    float tests = 0;
    bool answer, checked;

    for(begin = 0; begin < length; begin++)
        {
            counter = begin + 1;

            for(counter; counter < length; counter ++)
                {
                    if (test[begin] == test[counter])
                        {
                            tests += 1;

                        }
                    else if (test[begin] != test[(counter)])
                        {
                            continue;
                        }
                }
            cout << tests << endl;
        }

    if (tests > (length/2))
        {
            answer = false;
        }
    else if (tests == (length/2))
        {
            answer = true;
        }
    else if (tests == 0)
        {
            answer = false;
        }


    return answer;
}
