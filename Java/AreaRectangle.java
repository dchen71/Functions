
// This program lets you calculate the area of a rectangle
//   Inputs  : width,length
//   Outputs : width, length, area

/**
You must complete this program by providing 4 methods
so it calculates and displays the area of a rectangle.
*/

import java.util.Scanner;
import java.text.DecimalFormat;

public class AreaRectangle
{

    public static void main(String[] args)
    {
        double length, // The rectangle's length
        width, // The rectangle's width
        area; // The rectangle's area

        // Get the rectangle's length from the user.
        length = getLength();

        // Get the rectangle's width from the user.
        width = getWidth();

        // Get the rectangle's area.
        area = getArea(length, width);

        // Display the rectangle data.
        displayData(length, width, area);
    }


/**
Gets the length of the rectangle
@return The length of the rectangle
*/

public static double getLength()
    {
        double length;
        Scanner keyboard = new Scanner(System.in);

        System.out.println("Enter the rectangle's length: ");
        length = keyboard.nextDouble();
        while (length <= 0)
        {
            System.out.println("Invalid length, please try again");
            length = keyboard.nextDouble();
        }
        return length;
    }

/**
Gets the width of the rectangle
@return The width of the rectangle
*/

public static double getWidth()
    {
        double width;
        Scanner keyboard = new Scanner(System.in);

        System.out.println("Enter the rectangle's width: ");
        width = keyboard.nextDouble();
        while (width <= 0)
        {
            System.out.println("Invalid width, please try again");
            width = keyboard.nextDouble();
        }
        return width;
    }

/**
Calculates the area of the rectangle
@param length The length of the rectangle
@param width The width of the rectangle
@return The length of the rectangle
*/

public static double getArea(double length, double width)
    {
        return length * width;
    }

/**
Displays the width, length, and area of the rectangle
@param length The length of the rectangle
@param width The width of the rectangle
@param area The area of the rectangle
*/

public static void displayData(double length, double width, double area)
    {
        DecimalFormat decimals = new DecimalFormat("#0.00");

        System.out.println("The length is " + decimals.format(length) + ", the width is " + decimals.format(width)
                           + " and the area is " + decimals.format(area) + ".\n");
    }

}
