#include <iostream>

using namespace std;

template <class T>
class valuePair {
    T one, two;
  public:
    valuePair();
    valuePair(T item1, T item2);
    T getItem1();
    void setItem1(T uno);
    T getItem2();
    void setItem2(T dos);
};

template <class T>
valuePair<T>::valuePair ()
{
  one = 0;
  two = 0;
}

template <class T>
valuePair<T>::valuePair (T item1, T item2)
{
  one = item1;
  two = item2;
}

template <class T>
T valuePair<T>::getItem1 ()
{
  return one;
}

template <class T>
void valuePair<T>::setItem1 (T uno)
{
  one = uno;
}

template <class T>
T valuePair<T>::getItem2 ()
{
  return two;
}

template <class T>
void valuePair<T>::setItem2 (T dos)
{
  two = dos;
}
