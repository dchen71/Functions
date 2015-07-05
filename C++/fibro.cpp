//This program displays the Fibonacci Numbers

//Fn=F(n-1)+F(n-2)

#include <iostream>
#include <iomanip>
using namespace std;

//Function Prototypes
void askNum();
int fibo(int);

int main()
{
    int start, finish;
    int numZero = 0,numOne = 0;

    do
    {
        askNum();          //Calls the statement asking what number the user wants
        cin >> finish;

        while (finish < 0)
            {
                cout << "The number entered must be greater than or equal to zero\n";
                askNum();          //Calls the statement asking what number the user wants
                cin >> finish;
            }

    }
    while (finish < 0);

for (start = 0; start <= finish; start++)
    {
        cout << fibo(start);                   //Calls forth the function that displays the calculated number
        if (start < finish)
            {
                cout << ", ";
            }
        else if (start == finish)
            {
                cout << "...\n";
            }
    }

	return 0;
}


//Definition of the function askNum which asks what the number the user wants
void askNum()
{
    cout << "Which Fibonacci number do you want to find?\n";
}


//Definition of the function fibo which calculates the fibonacci numbers from the user inputted number
int fibo(int number)
{
    int fibonacci;
    static int fN_One,fN_Two;

    fibonacci = fN_One + fN_Two;
    if (number == 0)
        fibonacci = 0;
    else if (number == 1)
        fibonacci = 1;

    fN_One = fN_Two;
    fN_Two = fibonacci;

    return fibonacci;
}
