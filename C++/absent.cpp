//This program calculates the number of days a company's employees are absent

#include <iostream>
#include <iomanip>
using namespace std;

//Function Prototypes
void askEmployee();
int daysOut(int);
float averageDays(int, int);

int main()
{
    int employees;
    int numberEmployee,totalMissed;
    double avgDaysMissed;

do
    {
        askEmployee();                          //Displays the function to ask how many employees are in the company
        cin >> employees;
        while (employees < 1)
            {
                cout << "Number of employees must be one or greater.\n";
                askEmployee();                  //Displays the function to ask how many employees are in the company
                cin >> employees;
            }

    }
while (employees < 1);

totalMissed = daysOut(employees);                              //Determines the number of days the employees were out


cout << "The average number of days missed per employee is " << averageDays(totalMissed, employees) << ".\n";              //Calculates the average


	return 0;
}


//Definition of the function askEmployee which asks how many employees are in the company
void askEmployee()
{
    cout << "How many employees does the company have? \n";
}

int daysOut(int employees)
{
    int totalDays = 0;
    int days;
    int numberEmployee;

for (numberEmployee = 1; numberEmployee <= employees;numberEmployee++)
    {
        cout << "Days missed by Employee #" << numberEmployee << "?\n";
        cin >> days;

        if (days < 0)
            {
                cout << "Days missed must be zero or greater.\n";
                numberEmployee--;
                continue;
            }

        totalDays = days + totalDays;
    }

   return totalDays;
}

//Definition of the function average which calculates the average days missed by the employees
float averageDays(int totalMissed, int employees)
{

    return (float(totalMissed) / employees);
}

