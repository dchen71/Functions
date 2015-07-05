#include <iostream>
#include "Range.h"

using namespace std;

int main()
{
Range r1;

r1.setLowerLimit(5);
r1.setUpperLimit(20);

Range *p;
p = new Range();

p->setLowerLimit(1);
p->setUpperLimit(100);

int test = 15;

if(p->contains(test) == true)
    cout << "p contains 15!";
else if(p->contains(test) == false)
    cout << "p does not contains 15!";

int start;

Range r2[3];

for (start = 0; start < 3; start++)
    {
       r2[start].setUpperLimit(0);
       r2[start].setLowerLimit(10);
    }
return 0;
}
