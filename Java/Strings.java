
// This program lets you find out information about a name
//   Inputs  : string1, string2, char1, position
//   Outputs :

import java.util.Scanner;

public class Strings
{

    public static void main(String[] args)
    {
        Scanner keyboard = new Scanner(System.in);

        int position;
        char char1;
        String string1, string2;

        System.out.println("Enter first string: ");
        string1 = keyboard.nextLine();

        System.out.println("Enter second string: ");
        string2 = keyboard.nextLine();

        if (string1.compareToIgnoreCase(string2) > 0)
            System.out.println(string1 + " is greater than " + string2 + ".");
        else if (string1.compareToIgnoreCase(string2) < 0)
            System.out.println(string1 + " is greater than " + string2 + ".");
        else if (string1.compareToIgnoreCase(string2) == 0)
            System.out.println("Both strings are the same lenth");

        System.out.println("Number of characters in " + string1 +
                           " is " + string1.length());

        System.out.println("Enter position noting first character is at 0: ");
        position = keyboard.nextInt();

        // Get the character that is in the positon of string1
        char1 = showChar(string1, position);

        System.out.println("Character at position " + position + " in " +
                           string1 + " is: " + char1);

    }


/**
Get the character that is in the position of string1
@param s The first string
@param pos The character positon in the string
*/

public static char showChar(String s, int pos)
    {
        char letter;

        letter = s.charAt(pos);

        return letter;
    }

}
