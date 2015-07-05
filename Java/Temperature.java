/*
Algorithm: Temperature -
Creates private variables for building temperature
Has four constructors for four different situtations
Has three debugging writing methods
Has two accessor methods that write the temperature in Celsius and Farenheit respectively
Has three mutator methods to set parameters
Has a bool method to test temperatures for equality
Has a string method to return the temperature in string format
Has a input reader to read input
*/

import java.awt.*;
import java.util.Scanner;

public class Temperature
{
   private double degrees;
   private char type;

//Constructor for degrees and type
   public Temperature (double tempDegree, char tempType)
   {
      degrees = tempDegree;
      type = tempType;
   }

//Constructor for the degrees
   public Temperature (double tempDegree)
   {
      degrees = tempDegree;
      type = 'C';
   }

//Constructor for the type
   public Temperature (char tempType)
   {
      degrees = 0.0;
      type = tempType;
   }

//Default constructor
   public Temperature ()
   {
      degrees = 0.0;
      type = 'C';
   }

//Write method to show both parameter values
   public void writeOutput ()
   {
        if (type == 'C' || type == 'c')
            writeC();
        else
            writeF();
   }

//Displays temperature in C
   public void writeC ()
   {
        if (type == 'C' || type == 'c')
            System.out.println ("Temperature: " + degrees + "C");
        else
            System.out.println ("Temperature: " + getC() + "C");
   }

//Displays temperature in F
   public void writeF ()
   {
        if(type == 'F' || type == 'f')
            System.out.println ("Temperature: " + degrees + "F");
        else
            System.out.println ("Temperature: " + getF() + "F");
   }

//Celsius Accessor
   public double getC ()
   {
        if(type == 'F' || type == 'f')
            return Math.round(((degrees - 32) * 5/9) * 10)/10.0;
        else
            return degrees;
   }

//Fahrenheit Accessor
   public double getF ()
   {
        if(type == 'F' || type == 'f')
            return degrees;
        else
            return Math.round(((degrees * 9/5) + 32) * 10)/10.0;
   }

//Degrees mutator
   public void set(double d)
   {
      degrees = d;
   }


//Type mutator
   public void set(char t)
   {
      type = t;
   }

//Degree and type mutator
   public void set(double d, char t)
   {
      degrees = d;
      type = t;
   }

//Compares if the temperatures are the same
   public boolean equals(Temperature temp1)
   {
        if(this.getC() == temp1.getC() || this.getC() == temp1.getF())
            return true;
        else
            return false;
    }

//Displays the temperature in a string
   public String toString ()
   {
        String string1 = ("Temp: " + degrees + type);
        return string1;
   }

//Reads the input
   public void readInput ()
   {
        String tType;
        Scanner scan = new Scanner(System.in);

        System.out.println ("Please enter the numeric temperature: ");
        degrees = scan.nextDouble();

        System.out.println ("Please input the temperature type((C)elcius or (F)ahrenheit): ");
        Scanner scanS = new Scanner(System.in);
        tType = scanS.nextLine();
        type = tType.charAt(0);
   }

}
