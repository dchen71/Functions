//This program prints the outline of a parallelogram

#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
    int height, width;
    int widthMarker;
    int heightMarker;
    char character;

    cout << "What is the height of you parallelogram? \n";
    cin >> height;
    cout << "What character do you want to print? \n";
    cin >> character;

    cout << endl;

    width = height * 2;


    for (heightMarker = 1; heightMarker <= height; heightMarker++)
        {
                if (heightMarker == 1 || heightMarker == height)
                    {
                        for (widthMarker = 1; widthMarker <= width; widthMarker++)                //For the width of the top and bottom
                            {
                                    if (widthMarker < width)
                                        {
                                            cout << character;
                                        }
                                    else if (widthMarker == width)
                                        cout << character << endl;
                            }
                    }
                else if (heightMarker < height)
                    {
                        for (widthMarker = 1; widthMarker <= width; widthMarker++)                //For the Middle
                            {
                                    if (widthMarker == 1)
                                        {
                                            cout << character;
                                        }
                                    else if (widthMarker < width)
                                        {
                                            cout<< " ";
                                        }
                                    else if (widthMarker == width)
                                        {
                                            cout << character << endl;
                                        }
                            }
                    }

        }

	return 0;
}
