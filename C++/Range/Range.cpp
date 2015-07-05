#include <iostream>
#include "Range.h"

using namespace std;

Range::Range()
      {
            lower = 0;
            higher = 0;
            between = false;
      }

void Range::setLowerLimit(int value)
     {
            lower = value;
     }
int Range::getLowerLimit()
     {
         return lower;
     }
void Range::setUpperLimit(int value)
     {
           higher = value;
     }
int Range::getUpperLimit()
    {
           return higher;
      }
bool Range::contains(int value)
     {
      if (value >= lower && value <= higher)
             between = true;
      else
          between = false;

      return between;
     }
