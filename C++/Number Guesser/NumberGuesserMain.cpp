#include <iostream>
#include "NumberGuesser.h"

using namespace std;

int main() {

int low;
do
{
    cout << "What is the lowest non-negative number that the number can be?" << endl;

    cin >> low;
    if (low < 0)
        cout << "Please enter a number 0 or greater" << endl;
    else
        continue;
} while (low < 0);

int high;

do
{
    cout << "What is the highest number that the number can be?" << endl;

    cin >> high;

    if (high <= low)
        cout << "Please enter a number greater than the lowest number" << endl;
    else
        continue;
} while (high <= low);

NumberGuesser guesser(low, high);

cout << "Now think of a number between " << low << " and " << high << endl;

char checker;
char restart = 'y';



do
{

cout << "Is the number " << guesser.getCurrentGuess() << "? ([h]iger/[l]ower/[c]orrect)" << endl;
cin >> checker;
switch(checker)
{
    case 'h':
        guesser.higher();
        break;
    case 'H':
        guesser.higher();
        break;
    case 'l':
        guesser.lower();
        break;
    case 'L':
        guesser.lower();
        break;
    case 'c':
        cout << "You picked " << guesser.getCurrentGuess() << "? Good pick" << endl;
        guesser.reset();
        cout << "Do you want to play again?(y/n)" << endl;
        cin >> restart;
        break;
    case 'C':
        cout << "You picked " << guesser.getCurrentGuess() << "? Good pick" << endl;
        guesser.reset();
        cout << "Do you want to play again?(y/n)" << endl;
        cin >> restart;
        break;
    default:
        cout << "Please try again" << endl;
        break;
}
}while(restart == 'y');

return 0;
}
