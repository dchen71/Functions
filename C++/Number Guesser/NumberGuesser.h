#ifndef NumberGuesser_H
#define NumberGuesser_H

class NumberGuesser
{
private:
    int high;
    int low;
    int current;
    int higho;
    int lowo;

public:
    NumberGuesser(int lowerBound, int upperBound);

    void higher();
    void lower();
    int getCurrentGuess();
    void reset();
};
#endif
