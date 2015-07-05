//This program calculates Jackalope Populations

#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
    int initial, generation;
    const float DEATH = .01;    //Death rate
    const float BIRTH = .03;    //Birth rate
    int cycle = 1;
    float alive;
    int dead;
    int total;

    cout << "How many jackalopes do you have? \n";
    cin >> initial;
    cout << "How many generations do you want to wait? \n";
    cin >> generation;

    total = initial;

    while (cycle <= generation)
        {
            alive = total + (total * BIRTH);
            dead = (alive * DEATH);
            total = alive - dead;
            cycle++;
        }


    cout << "If you start with " << initial << " jackalopes and wait "
         <<  generation << " generations,\n";
    cout << "you will end up with a total of " << total << " jackalopes. \n";

	return 0;
}
