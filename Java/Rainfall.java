
// This program demonstrates my ability to use an array to store values in a program
//   Inputs  : monthlyRain
//   Outputs : totalRainfall, monthlyRain, majorRain, privateRain

import java.util.Scanner;
import java.text.DecimalFormat;

public class Rainfall
{

    public static void main(String[] args)
    {
        Scanner keyboard = new Scanner(System.in);
        DecimalFormat decimals = new DecimalFormat("#0.0");

        double[] monthlyRain;
        int months = 12;
        monthlyRain = new double[months];

        int start = 0;
        double totalRainfall, monthlyRainfall;
        int majorRain, privateRain;

        for(start = 0; start < 12; start++)
        {
                initRain((start + 1));
                monthlyRain[start] = keyboard.nextDouble();
                    while(monthlyRain[start] < 0)
                    {
                        System.out.println("Please input a value" +
                                            " greater than zero");
                        initRain((start + 1));
                        monthlyRain[start] = keyboard.nextDouble();
                    }
        }


        totalRainfall = totalRain(monthlyRain);
        System.out.println("The total rainfall for this year is "
                           + decimals.format(totalRainfall));

        monthlyRainfall = averageRain(totalRainfall);
        System.out.println("The avergage rainfall for this year is "
                           + decimals.format(monthlyRainfall));

        majorRain = mostRain(monthlyRain);
        System.out.println("The month with the highest amount of rain is "
                           + (majorRain + 1));

        privateRain = leastRain(monthlyRain);
        System.out.println("The month with the lowest amount of rain is "
                           + (privateRain + 1));
    }


/**
Starts asking the amount of rain recorded in a month
@param month The month
*/

public static void initRain(int month)
{
        System.out.print("Enter rain fall for month " + month + ": ");
}


/**
Finds out the total amount of rain
@param rain The array with the amount of rain in a month
@return totalRain Returns the total amount of rain in a year
*/

public static double totalRain(double[] rain)
{
    double totalRain = 0;
    int start = 0;

    for(start = 0;start < 12; start++)
        totalRain = rain[start] + totalRain;

    return totalRain;
}


/**
Finds out the average rain in a month
@param rainfall The total amount of rainfall in a year
@return average Returns the average amount of rain per month
*/

public static double averageRain(double rainfall)
{
    double average;

    average = rainfall / 12;

    return average;
}


/**
Get the character that is in the position of string1
@param rainfall The rainfall array
@return pos The position of the greatest raining month
*/

public static int mostRain(double[] rainfall)
{
    int pos = 0;
    int start;

    for(start = 0; start < 12; start++)
        {
            if (rainfall[start] > rainfall[pos])
                pos = start;
            else if (rainfall[start] == rainfall[pos])
                pos = start;
            else if (rainfall[start] < rainfall[pos])
                continue;
        }

    return pos;
}


/**
Get the character that is in the position of string1
@param rainfall The rainfall array
@return pos The position of the lowest raining month
*/

public static int leastRain(double[] rainfall)
{
    int pos = 0;
    int start = 0;

    for(start = 0; start < 12; start++)
    {
        if (rainfall[start] < rainfall[pos])
            pos = start;
        else if (rainfall[start] == rainfall[pos])
            pos = start;
        else if (rainfall[start] > rainfall[pos])
            continue;
    }

    return pos;
}

}
