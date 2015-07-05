#include <iostream>
#include "valuePair.h"

using namespace std;

int main() {
valuePair<int> pi;
valuePair<char> pc;
valuePair<string*> ps;

// these lines should print out "5 900"
pi.setItem1(5);
pi.setItem2(900);
cout << pi.getItem1() << " ";
cout << pi.getItem2() << endl;

// these lines should print out "z z"
pc.setItem1('z');
pc.setItem2('z');
cout << pc.getItem1() << " ";
cout << pc.getItem2() << endl;

// these lines should print out "fast car"
ps.setItem1(new string("fast"));
ps.setItem2(new string("car"));
cout << *ps.getItem1() << " ";
cout << *ps.getItem2() << endl;

// these lines should print out "999.9 88.8"
// this is the two argument constructor
valuePair<float> pf(999.9, 88.8);
cout << pf.getItem1() << " ";
cout << pf.getItem2() << endl;


return 0;
}
