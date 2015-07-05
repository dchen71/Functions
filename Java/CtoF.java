
// This program displays a table of Celsius temperaturs and their Fahrenheit equivalents
//   Inputs  :
//   Outputs : table

public class CtoF {

   public static void main (String[] args)
    {
       double fah, cel;
       final double CONV = (9.0/5.0);        // 9/5 Constant

       System.out.print("\n");
       System.out.println("   Centrigrade \t     Fahrenheit");
       System.out.println("---------------   ----------------");

       for (cel = 0; cel <= 20; cel++)
       {
           fah = (CONV * cel) + 32;
           fah = Math.round(fah);
           System.out.println("\t" + (int)cel + "\t \t" + (int)fah);
       }

       System.out.print("\n");
    }
}
