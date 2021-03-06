// ENABLE ASSERTIONS

import java.io.Serializable;

/**
 * A class that implements the ADT list by using a fixed-size array.
 */
public class AList<T extends Comparable> implements ListInterface<T>, Serializable {
	private T[] list; // array of list entries
	private int length; // current number of entries in list
	private static final int MAX_SIZE = 50; // max length of list

	public AList() {
		this(MAX_SIZE); // call next constructor
	} // end default constructor

	public AList(int maxSize) {
		length = 0;
		list = (T[]) new Comparable[maxSize]; // necessary cast to generic type
	} // end constructor

    public AList(T[] origArray)
    {
        ListInterface<T> list = new AList<T>();
        int length = origArray.length;

        for(int start = 0; start < length; start++)
        {
            list.add(origArray[start]);
        }
    }

	public boolean add(T newEntry) {
		boolean isSuccessful = true;

		if (!isFull()) {
			// Assertion: Length of list < length of array
			assert length < list.length;

			// position of new entry will be after last entry in list,
			// that is, at position length+1; corresponding array index is
			// 1 less than this position, so index is length
			list[length] = newEntry;
			length++;
		} else
			isSuccessful = false;

		return isSuccessful;
	} // end add

	public boolean add(int newPosition, T newEntry) {
		boolean isSuccessful = true;

		if (!isFull() && (newPosition >= 1) && (newPosition <= length + 1)) {
			makeRoom(newPosition);
			list[newPosition - 1] = newEntry;
			length++;
		} else
			isSuccessful = false;

		return isSuccessful;
	} // end add

	public T remove(int givenPosition) {
		T result = null; // return value

		if ((givenPosition >= 1) && (givenPosition <= length)) {
			assert !isEmpty();
			result = list[givenPosition - 1]; // get entry to be removed

			// move subsequent entries toward entry to be removed,
			// unless it is last in list
			if (givenPosition < length)
				removeGap(givenPosition);

			length--;
		} // end if

		return result; // return reference to removed entry, or
						// null if either list is empty or givenPosition
						// is invalid
	} // end remove

	public void clear() {
		for (int index = 0; index < length; index++)
			// loop is part of Q4
			list[index] = null;

		length = 0; // no need to create a new array
	} // end clear

	public boolean replace(int givenPosition, T newEntry) {
		boolean isSuccessful = true;

		if ((givenPosition >= 1) && (givenPosition <= length)) // test catches
																// empty list
		{
			assert !isEmpty();
			list[givenPosition - 1] = newEntry;
		} else
			isSuccessful = false;

		return isSuccessful;
	} // end replace

	public T getEntry(int givenPosition) {
		T result = null; // result to return

		if ((givenPosition >= 1) && (givenPosition <= length)) {
			assert !isEmpty();
			result = list[givenPosition - 1];
		} // end if

		return result;
	} // end getEntry

	public boolean contains(T anEntry) {
		boolean found = false;

		for (int index = 0; !found && (index < length); index++) {
			if (anEntry.equals(list[index]))
				found = true;
		} // end for

		return found;
	} // end contains

	public int getLength() {
		return length;
	} // end getLength

	public boolean isEmpty() {
		return length == 0;
	} // end isEmpty

	public boolean isFull() {
		return length == list.length;
	} // end isFull

	public void display() {
		for (int index = 0; index < length; index++)
			System.out.println(list[index]);
	} // end display

	/**
	 * Task: Makes room for a new entry at newPosition. Precondition: 1 <=
	 * newPosition <= length + 1; length is list�s length before addition.
	 */
	private void makeRoom(int newPosition) {
		assert (newPosition >= 1) && (newPosition <= length + 1);

		int newIndex = newPosition - 1;
		int lastIndex = length - 1;

		// move each entry to next higher index, starting at end of
		// list and continuing until the entry at newIndex is moved
		for (int index = lastIndex; index >= newIndex; index--)
			list[index + 1] = list[index];
	} // end makeRoom

	/**
	 * Task: Shifts entries that are beyond the entry to be removed to the next
	 * lower position. Precondition: list is not empty; 1 <= givenPosition <
	 * length; length is list�s length before removal.
	 */
	private void removeGap(int givenPosition) {
		assert (givenPosition >= 1) && (givenPosition < length);

		// move each entry to next lower position starting at entry after the
		// one removed and continuing until end of list
		int removedIndex = givenPosition - 1;
		int lastIndex = length - 1;

		for (int index = removedIndex; index < lastIndex; index++)
			list[index] = list[index + 1];
	} // end removeGap

    public int getPosition(T anObject)
    {
        int position = 0;

        for(int start = 0; start < this.getLength(); start++)
        {
            if(this.getEntry(start + 1).equals(anObject) == true)
                {
                    position = start + 1;
                    start = this.getLength();
                }
        }

        return position;
    }

    public boolean remove(T anObject)
    {
        int length = this.getLength();
        boolean removed = false;

        for(int start = 0; start < length; start++)
        {
            if(this.getEntry(start + 1).equals(anObject) == true)
                {
                    this.remove((start + 1));
                    removed = true;
                    start = length;
                }
        }

        return removed;
    }

    public void moveToEnd()
    {
        ListInterface<T> list = new AList<T>();
        list.add(this.getEntry(1));
        this.remove(1);
        this.add(list.getEntry(1));
    }

    public T replaceAndReturn(int givenPosition, T anObject)
    {
        ListInterface<T> replaced = new AList<T>();

        replaced.add(getEntry(givenPosition));
        this.replace(givenPosition, anObject);

		return replaced.getEntry(1);
    }

@Override
    public boolean equals(Object obj)
    {
        boolean equal = false;

        if (obj instanceof AList)
        {
            ListInterface<T> otherList = (ListInterface<T>) obj;
            for (int start = 1; start <= otherList.getLength(); start++)
            {
                if(this.getEntry(start).compareTo(otherList.getEntry(start)) == 0)
                {
                    equal = true;
                }
                else
                {
                    equal = false;
                    start = this.getLength();
                }
            }
        }
        return equal;
    }

    public T getMin()
    {
        ListInterface<T> low = new AList<T>();
        low.add(this.getEntry(1));

        for(int start = 0; start < this.getLength() - 1; start++)
        {
            if(this.getEntry(start + 1).compareTo(this.getEntry(start + 2)) < 0)
                {
                    low.replace(1,this.getEntry(start + 1));
                }
            else if(this.getEntry(start + 1).compareTo(this.getEntry(start + 2)) > 0)
                {
                    low.replace(1 ,this.getEntry(start + 2));
                }
        }
        return low.getEntry(1);
    }

    public T removeMin()
    {
        ListInterface<T> min = new AList<T>();
        min.add(this.getMin());

        int position = getPosition(min.getEntry(1)); //getPosition from problem 2

        this.remove(position);

        return min.getEntry(1);
    }

} // end AList

