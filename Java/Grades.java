
// This program lets you input numbers
//   Inputs  : number
//   Outputs : largest, smallest

import java.util.Scanner;
public class Grades {

   public static void main (String[] args)
    {
       int largest, smallest, number;
       Scanner keyboard = new Scanner(System.in);

       System.out.print("Enter an integer, or -99 to quit: ");
       number = keyboard.nextInt();

       if (number == -99)
            System.out.println("You did not enter any numbers.");
       else
       {
            largest = number;
            smallest = 0;

            //Sentinel value loop
            while (number != -99)
            {

                  System.out.print("Enter an integer, or -99 to quit: ");
                  number = keyboard.nextInt();

            //Assignment
                  if (largest < number)
                     {
                        smallest = largest;
                        largest = number;
                     }
                  else if (largest > number && number > -99)
                        smallest = number;
                  else;

            }

            System.out.print("Largest: " + largest + "\n");
            System.out.print("Smallest: " + smallest + "\n");

        }

    }
}
