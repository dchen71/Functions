//This program checks for palindromes

#include <iostream>
#include <iomanip>
#include <cstring>

using namespace std;

//Function Prototypes
bool palindrome(char[31]);

int main()
{
    char word[31];
    bool answer;

    cout << "Please enter a word:\n";
    cin >> word;

    answer = palindrome(word);

    if (answer == true)
        cout << "\"" << word << "\" is a palindrome.\n";
    else if (answer == false)
        cout << "\"" << word << "\" is not a palindrome.\n";


	return 0;
}


//Definition of the function palindrome which checks to see if the user inputted word is a palindrome
bool palindrome(char forward[31])
{
    bool answer;
    int length = strlen(forward);
    char backwards[(length + 1)];
    int start, answerNum;

    for(start = 0; start < length;start++)
        {
            backwards[start] = forward[length - 1 - start];
        }

    answerNum = strcmp(forward,backwards);

        if (answerNum == 0)
            answer = true;
        else if (answerNum != 0)
            answer = false;

    return answer;
}
