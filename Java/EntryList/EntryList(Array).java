public class EntryList<T> implements EntryWayListInterface<T>
{

    private int length;
    private T[] list;
    private static final int maxSize = 11;

    public EntryList()
    {
        length = 0;
        list = (T[]) new Object[maxSize];
    }

    public EntryList(int size)
    {
        length = 0;
        list = (T[]) new Object[size];
    }

    public EntryList(T[] items, int numItem)
    {
        length = numItem;

        if(numItem < maxSize)
        {
            list = (T[]) new Object[maxSize];
        }
        else
            list = (T[]) new Object[numItem *2];

        for(int start = 1; start <= length; start++)
        {
            list[start] = items[start - 1];
        }
    }

  /** Task: Adds a new entry to the first member of the list.
   *  @param newEntry - the object to be added as a new entry
   *  @return true if newEntry added to the head of the list otherwise false if unable to */
    public boolean insertHead(T newEntry)
    {
        boolean added = false;

        if(isEmpty())
        {
            list[1] = newEntry;
            added = true;
            length++;
        }
        else
        {
            if(isFull())
            {
                T[] oldList = (T[]) new Object[list.length];
                oldList = list;
                list = (T[]) new Object[2 * length];

                for(int index = 1; index < oldList.length; index++)
                {
                    list[index] = oldList[index];
                }

                length = length + 1;

                for(int start = 1; start <= length; start++)
                {
                    list[length - start + 1] = list[length - start];
                }
                list[1] = newEntry;
                added = true;
            }

            else
            {
                ++length;

                for(int start = 1; start <= length; start++)
                {
                    list[length - start + 1] = list[length - start];
                }

                list[1] = newEntry;
                added = true;
            }
        }

        return added;
    }


  /** Task: Adds a new entry at the tail end of the list
   *  @param newEntry - the object to be added to the end of the list
   *  @return true if newEntry added to the tail end of the list otherwise false if unable to */
    public boolean insertTail(T newEntry)
    {
        boolean added = false;

        if(isEmpty())
        {
            list[1] = newEntry;
            added = true;
            length++;
        }
        else
        {
            if(!isFull())
            {
                list[length + 1] = newEntry;
                added = true;
                length++;
            }
            else
            {
                T[] oldList = (T[]) new Object[list.length];
                oldList = list;
                list = (T[]) new Object[2 * length];

                for(int index = 1; index < oldList.length; index++)
                {
                    list[index] = oldList[index];
                }

                list[length + 1] = newEntry;
                added = true;
                length++;
            }
        }

        return added;
    }


  /** Task: Deletes the 1st member of the list
  *   @return returns the object that you had deleted from the list */
    public T deleteHead()
    {
        T head = null;

        if(!isEmpty())
        {
            head = list[1];

            for(int start = 1; start <= length; start ++)
            {
                list[start] = list[start + 1];
            }
            length--;
        }


        return head;
    }


  /** Task: Deletes the tail end of the list
  *   @return returns the object that you had deleted from the list */
    public T deleteTail()
    {
        T tail = null;

        if(length > 0)
        {
            tail = list[length];

            list[length] = null;
            length--;
        }



        return tail;
    }


  /** Task: Displays the entries in the list */
    public void display()
    {
        for(int start = 1;start <= length; start++)
        {
            System.out.println(list[start]);
        }
    }


  /** Task: Sees whether the list contains a given entry.
   *  @param anEntry - the object that will be checked against the list
   *  @return returns position where anEntry was found */
    public int contains(T anEntry)
    {
        int position = 0;

        if(length != 0)
        {
            for(int start = 1; start <= length; start++)
            {
                if(list[start].equals(anEntry) == true)
                {
                    position = start;
                    start = length;
                }
            }
        }

        return position;
    }


  /** Task: Checks if the list is empty
   *  @return true if list is empty, otherwise false */
    public boolean isEmpty()
    {
        boolean empty = false;

        if(length == 0)
            empty = true;

        return empty;
    }


  /** Task: Checks if the list is full
   *  @return true if list is full, otherwise false */
    public boolean isFull()
    {
        boolean full = false;

        if(length == list.length - 1)
            full = true;

        return full;
    }

}
