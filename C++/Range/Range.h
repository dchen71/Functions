 #ifndef Range_H
#define Range_H

class Range
{
private:
int lower;
int higher;
bool between;

public:
Range();

void setLowerLimit(int value);
int getLowerLimit();
void setUpperLimit(int value);
int getUpperLimit();
bool contains(int value);
};
#endif

