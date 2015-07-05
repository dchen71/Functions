//This program lets you play blackjack

#include <iostream>
#include <cstdlib>

using namespace std;

//Function prototypes
void results(int, int);
int hitme();


int main()

{

    int p_total, d_total;
    char again;

    do
    {
        d_total = (rand()%(10-1+1)+1);
        p_total = 0;

        cout << "The dealer starts with a " << d_total << endl;

        p_total = hitme();

        if(p_total > 21)
        {
            cout << endl << "Play again? (y/n): ";
            cin >> again;
        }
        else if (p_total <= 21)
        {
            results(p_total, d_total);

            cout << endl << "Play again? (y/n): ";
            cin >> again;
        }

    }
    while (again == 'Y' || again == 'y');




    return 0;

}

void results(int player, int dealer)
{
    char confirm;
    int dealerhit;

    cout << "Dealers has a " << dealer << "..." << endl;

    do
    {
        cout << "(c to continue) c" << endl;
        cin >> confirm;
    }
    while (confirm != 'c');

    while (dealer < 17)
    {
        if (dealer > 21)
        {
            cout << "Dealer busts" << endl;
            break;
        }

        dealerhit = (rand()%(10-1+1)+1);
        dealer += dealerhit;
        cout << "Dealer gets a " << dealerhit << endl;
        cout << "Total: " << dealer << endl;

    }

    if (dealer == player)
        {
            cout << "Push!" << endl;
        }
    else if (dealer > player && dealer <= 21)
        {
            cout << "Dealer Wins!" << endl;
        }
    else if (player > dealer)
        {
            cout << "Player Wins!" << endl;
        }
}

int hitme()
{
    int total, card[20];
    char hit;
    int counter = 2;

    card[0] = (rand()%(10-1+1)+1);
    card[1] = (rand()%(10-1+1)+1);

    total = card[0] + card[1];

    cout << "Your first cards: " << card[0] << ", " << card[1] << endl;
    cout << "Total: " << total << endl;

    cout << "hit? (y/n): ";
    cin >> hit;

/*
        while (hit == 'y' || hit == 'Y')
        {

            card[counter] = (rand()%(11-1+1)+1);
            total += card[counter];

            cout << "Card: " << card[counter] << endl;
            cout << "Total: " << total << endl;

            if (total > 21)
            {
                cout << "Player busts" << endl;

                char repeat;

                do
                {
                    cout << endl << "Play again? (y/n): ";
                    cin >> repeat;
                    if (repeat == 'n' || repeat == 'N')
                        {
                            break;
                        }
                }
                while (repeat != 'y');
            }
            else if (total <= 21)
            {
                counter += 1;

                cout << "hit? (y/n) " << endl;
                cin >> hit;
            }
        }
*/

        while (hit == 'y' || hit == 'Y')
        {

            card[counter] = (rand()%(11-1+1)+1);
            total += card[counter];

            cout << "Card: " << card[counter] << endl;
            cout << "Total: " << total << endl;

            if (total > 21)
            {
                cout << "Player busts" << endl;
                break;
            }
                counter += 1;

                cout << "hit? (y/n) " << endl;
                cin >> hit;

        }

    return total;
}
