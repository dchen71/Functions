public class SortedList<T extends Comparable<? super T>>             implements SortedListInterface<T>{  private ListInterface<T> list;  public SortedList()  {    list = new LList<T>();  } // end default constructor
    public boolean add(T newEntry)
    {
        boolean added = false;
        int position = getPosition(newEntry);

        if(!isFull())
        {
            if(position < 0)
            {
                position = Math.abs(position);
                list.add(position, newEntry);
                added = true;
            }

            else
            {
                added = false;
            }
        }

        return added;
    }    public boolean remove(T anEntry)    {      boolean result = false;      int position = getPosition(anEntry);      if (position > 0)      {        list.remove(position);        result = true;      } // end if      return result;    } // end remove
    public boolean contains(T anEntry)
    {
		if(anEntry != null)
        {
            if(list.getLength() > 0)
            {
                boolean found = false;
                int current = 1;

                while (!found && (getEntry(current) != null))
                {
                    if (anEntry.equals(getEntry(current)))
                        found = true;
                    else if(getEntry(current + 1) != null && anEntry.compareTo(getEntry(current)) > 0 && anEntry.compareTo(getEntry(current + 1)) < 0)
                    {
                        found = false;
                        break;
                    }
                    else
                        current += 1;
                }

                return found;
            }
            else
                return false;
        }
        else
            return false;
    }

    public int getPosition(T anEntry)    {      int position = 1;      int length = list.getLength();      // find position of anEntry      while ( (position <= length) &&              (anEntry.compareTo(list.getEntry(position)) > 0) )      {        position++;      } // end while      // see whether anEntry is in list      if ( (position > length) ||           (anEntry.compareTo(list.getEntry(position)) != 0) )      {        position = -position; // anEntry is not in list      } // end if      return position;    } // end getPosition
    public T getEntry(int givenPosition)    {      return list.getEntry(givenPosition);    } // end getEntry

	public int getLength() {
		return list.getLength();
	} // end getLength

	public boolean isEmpty() {
		return list.isEmpty();
	} // end isEmpty

	public boolean isFull() {
		return list.isFull();
	} // end isFull

	public void display() {
		list.display();
	} // end display

	public void clear() {
        list.clear();
	}

	public T remove(int givenPosition) {
        return list.remove(givenPosition);
	}

} // end SortedList