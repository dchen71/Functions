/*
Algorithm: TwoSorts -
Initialize variables, general applet sizes, arrays
Checks to ensure that no repeated values are present for arrays
Paint draws the arrays
Two methods are to used to do an insertion sort and selection sort
Button is used to count the number of sorts and to allow the user to be able to continue the sorting
*/

import java.applet.Applet;
import java.awt.*;
import java.awt.event.*;
import java.util.Random;
import java.applet.*;

public class TwoSorts extends Applet
{
//Initialize variables, points, buttons
    private final int APPLET_WIDTH = 400;
    private final int APPLET_HEIGHT = 400;

    Button butn1 = new Button("Sort");
    Label lab = new Label("Click to sort");
    int sort = 0;

    Random randomGenerator = new Random();
    int[] inArray = new int[15];
    int[] selArray = new int[15];
    Boolean[] unique = new Boolean[31];
    static int inStart, selStart;

//Works as a constructor for the class
    public void init()
    {
        addMouseListener (new MouseHandler());

        setBackground (Color.blue);
        setSize (APPLET_WIDTH, APPLET_HEIGHT);

//Adds the buttons
        butn1.addActionListener(new Butn1Handler());
        add(butn1);
        add(lab);

//Checks for unique values
        for(int start = 0; start < 31; start++)
        {
            unique[start] = false;
        }
        unique[0] = true;

        for(int start = 0; start < 15; start++)
        {
            int temp = randomGenerator.nextInt(30);

            do
            {
                temp = randomGenerator.nextInt(30);
            }
            while(unique[temp] == true);

            inArray[start] = temp;
            selArray[start] = temp;
            unique[temp] = true;
        }

        inStart = 1;
        selStart = 0;
    }

//Draws the graphics
    public void paint (Graphics g)
    {
        if(inStart < 15 || selStart < 14)
            {
                insertionSort(inArray);
                inStart++;
                selectionSort(selArray);
                selStart++;

                for(int start = 0; start < 15; start++)
                    {
                        g.setColor(Color.black);
                        g.fillRect (10 + (20 * start) + (5 * start), 50, 20, inArray[start] * 4);
                        g.setColor(Color.green);
                        g.fillRect (10 + (20 * start) + (5 * start), 200, 20, selArray[start] * 4);
                    }
            }
        else
            {
                for(int start = 0; start < 15; start++)
                    {
                        g.setColor(Color.gray);
                        g.fillRect (10 + (20 * start) + (5 * start), 50, 20, inArray[start] * 4);
                        g.fillRect (10 + (20 * start) + (5 * start), 200, 20, selArray[start] * 4);
                    }
            }
    }

//Empty Methods
    private class MouseHandler implements MouseListener
    {
        public void mousePressed (MouseEvent event){}
        public void mouseClicked (MouseEvent event) {}
        public void mouseReleased (MouseEvent event) {}
        public void mouseEntered (MouseEvent event) {}
        public void mouseExited (MouseEvent event) {}
    }

//Buttons
    class Butn1Handler implements ActionListener
    {
        public void actionPerformed(ActionEvent e)
        {
            if(inStart < 15 && selStart < 14)
                {
                    sort++;
                    lab.setText("Sort: " + sort);
                    repaint();
                }
            else
                {
                    ++sort;
                    lab.setText("Sort complete");
                    remove(butn1);
                    repaint();
                }
        }
    }

//Insertion Sort Method
    public static void insertionSort (int[] list)
    {
        int position = inStart;
        int temp;
        while(position > 0 && list[position - 1] > list[position])
        {
            temp = list[position - 1];
            list[position - 1] = list[position];
            list[position] = temp;
            position--;
        }
    }

//Selection Sort method
    public static void selectionSort (int[] list)
    {
        int min;
        int temp;
        min = selStart;
        for (int scan = selStart + 1; scan < 15; scan++)
            if (list[scan] < list[min])
                min = scan;
// Swap the values
        temp = list[min];
        list[min] = list[selStart];
        list[selStart] = temp;
    }

//Selection sort searches for smallest from its start point and goes on, 1st ele = lowest, 2nd ele=2nd lowest, etc
//Insertion sort starts with 1 and searches directly right to see if greater, if smaller then insert in that positino and shift everything forward

