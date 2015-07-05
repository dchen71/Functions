#include <iostream>
#include "NumberGuesser.h"



using namespace std;


NumberGuesser::NumberGuesser(int lowerBound, int upperBound)
    {
        high = upperBound;
        low = lowerBound;
        higho = upperBound;
        lowo = lowerBound;
    }

void NumberGuesser::higher()
    {
        low = current + 1;
    }
void NumberGuesser::lower()
    {
        high = current - 0;
    }
int NumberGuesser::getCurrentGuess()
    {
        current = ((high + low)/2);
        return current;
    }
void NumberGuesser::reset()
    {
        high = higho;
        low = lowo;
    }
