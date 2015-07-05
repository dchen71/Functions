//This program accepts a string and returns the number of vowels in it

#include <iostream>
#include <cstring>
#include <string>

using namespace std;

int main()
{

    string word;
    int vowels = 0;
    int start = 0;

    cout << "Enter a string\n";
    cin >> word;

    int length = word.length();

    for(start = 0; start < length; start++)
    {
        if(word[start] == 'a' or word[start] == 'A')
        {
            vowels += 1;
        }
        else if(word[start] == 'a' or word[start] == 'A')
        {
            vowels += 1;
        }
        else if(word[start] == 'e' or word[start] == 'E')
        {
            vowels += 1;
        }
        else if(word[start] == 'i' or word[start] == 'I')
        {
            vowels += 1;
        }
        else if(word[start] == 'o' or word[start] == 'O')
        {
            vowels += 1;
        }
        else if(word[start] == 'u' or word[start] == 'U')
        {
            vowels += 1;
        }
    }

    cout << word << " has " << vowels << " vowels. " << endl;


    return 0;

}

