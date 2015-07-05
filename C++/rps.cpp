//This program lets you play Rock-Paper-Scissors

#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
	char playerOne, playerTwo;

	cout << endl;
	cout << "Player One, please enter your move:\n";
	cin >> playerOne;
	cin.ignore();
	cout << endl;
	cout << "Player Two, please enter your move:\n";
	cin >> playerTwo;
	cin.ignore();
    cout << endl;

    switch (playerOne)
    {
        case 'r':
        case 'R':
            {
                switch (playerTwo)
                {
                    case 'r':
                    case 'R': cout << "We have a tie. Neither player wins.\n";
                        break;
                    case 's':
                    case 'S': cout << "Player One wins. Rock dulls scissors!\n";
                        break;
                    case 'p':
                    case 'P': cout << "Player Two wins. Paper covers rock!\n";
                        break;
                    default:  cout << "Player Two has entered an illegal move. \n";
                        break;
                }
            }
            break;
        case 'p':
        case 'P':
            {
                switch (playerTwo)
                {
                    case 'r':
                    case 'R': cout << "Player One wins. Paper covers rock!\n";
                        break;
                    case 's':
                    case 'S': cout << "Player Two wins. Scissors cut paper!\n";
                        break;
                    case 'p':
                    case 'P': cout << "We have a tie. Neither player wins.\n";
                        break;
                    default:  cout << "Player Two has entered an illegal move. \n";
                        break;
                }
            }
            break;
        case 's':
        case 'S':
            {
                switch (playerTwo)
                {
                    case 'r':
                    case 'R': cout << "Player Two wins. Rock dulls scissors!\n";
                        break;
                    case 's':
                    case 'S': cout << "We have a tie. Neither player wins.\n";
                        break;
                    case 'p':
                    case 'P': cout << "Player One wins. Scissors cut paper!\n";
                        break;
                    default:  cout << "Player Two has entered an illegal move. \n";
                        break;
                }
            }
            break;
        default:
            {
                switch (playerTwo)
                {
                    case 'r':
                    case 'R': cout << "Player One has entered an illegal move. \n";
                        break;
                    case 's':
                    case 'S': cout << "Player One has entered an illegal move. \n";
                        break;
                    case 'p':
                    case 'P': cout << "Player One has entered an illegal move. \n";
                        break;
                    default:
                    {
                        cout << "Player One has entered an illegal move. \n";
                        cout << endl;
                        cout << "Player Two has entered an illegal move. \n";
                    }
                        break;
                }
            }

    }
	return 0;
}
