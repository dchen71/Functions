/*
ItemPair. Objects of this class hold a pair of two items that are the same type.
For example, an ItemPair can hold two Integers or it could hold two Strings or it could hold two ArrayLists, etc. An ItemPair could not, however, hold an Integer and a String.
*/

public class ItemPair<T>
{
    private T first, second;

//Constructor
    public ItemPair(T firstItem, T secondItem)
    {
        first = firstItem;
        second = secondItem;
    }

//Sets the first values
    public void setItem1(T firstItem)
    {
        first = firstItem;
    }

//Returns the first value
    public T getItem1()
    {
        return first;
    }

//Sets the second values
    public void setItem2(T secondItem)
    {
        second = secondItem;
    }

//Returns the second value
    public T getItem2()
    {
        return second;
    }

//Converts values into string
    public String toString()
    {
        String converted = "First:" + first + " Second:" + second;
        return converted;
    }

//Same memory location
    public boolean sameItems()
    {
        boolean same = false;
        if (first == second)
            same = true;

        return same;
    }

//Same value check
    public boolean equals(Object pair2)
    {
        boolean equiv = false;

        ItemPair test = (ItemPair) pair2;
        Object second1, second2;

        second1 = test.getItem1();
        second2 = test.getItem2();

        if (first == second1 && second == second2)
            equiv = true;

        return equiv;
    }
}
