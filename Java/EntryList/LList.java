// 1
/**
 * A class that implements the ADT list by using a chain of nodes.
 *
 * @author Frank M. Carrano
 * @version 2.0
 */
public class LList<T extends Comparable> implements ListInterface<T> {
	private Node firstNode; // reference to first node
	private int length; // number of entries in list

	public LList() {
		clear();
	} // end default constructor


    public LList(T[] origArray, int numEnt)
    {
        for(int start = 0; start < numEnt; start++)
        {
            this.add(origArray[start]);
        }
    }

	public final void clear() // NOTICE clear cannot be final in interface
	{
		firstNode = null;
		length = 0;
	} // end clear

    public void addAll(T[] items)
    {
        int arrayLen = items.length;

        for(int start = 0; start < arrayLen; start++)
        {
            this.add(items[start]);
        }
    }

    public int getPosition(T anObject)
    {
        int position = 55;

        for(int start = 1; start <= length; start++)
        {
            if (this.getEntry(start).equals(anObject) == true)
            {
                position = start;
                start = length;
            }
            else
            {
                position = 0;
            }
        }

        return position;
    }

@Override
    public boolean equals(Object obj)
    {
        boolean equal = false;

        if (obj instanceof LList)
        {
            LList<T> otherList = (LList<T>) obj;

            if(this.getLength() < otherList.length || this.getLength() > otherList.length)
            {
                equal = false;
            }
            else
            {
                for (int start = 1; start <= otherList.length; start++)
                {
                    if(this.getEntry(start).equals(otherList.getEntry(start)) == true)
                    {
                        equal = true;
                    }
                    else
                    {
                        equal = false;
                        start = otherList.length;
                    }
                }
            }

        }
        return equal;
    }





    public LList<T> getAllLessThan(Comparable<T> anObject)
    {
        LList<T> low = new LList<T>();

        for(int start = 1; start <= length; start++)
        {
            if(this.getEntry(start).compareTo(anObject) < 0)
            {
                low.add(this.getEntry(start));
            }
        }

        return low;
    }

    public boolean remove(T anObject)
    {
        boolean removed = false;

        for(int start = 1; start <= length; start++)
        {
            if(this.getEntry(start).equals(anObject) == true)
                {
                    this.remove((start));
                    removed = true;
                    start = length;
                }
        }

        return removed;
    }

    public void moveToEnd()
    {
        this.add(getEntry(1));
        this.remove(1);
    }

    public T getMin()
    {

        T smallest = null;

        if (length > 0)
        {
            smallest = this.getEntry(1);
            for (int index = 1; index <= length; index++)
            {
                T item = this.getEntry(index);
                if (item.compareTo(smallest) < 0)
                    smallest = item;
            }
        }
      return smallest;
     }

    public T removeMin()
    {
        T smallest = null;

        if (!isEmpty())
        {
            smallest = getEntry(1);
            int smallestPosition = 1;
            for (int index = 2; index <= length; index++)
            {
                T item = getEntry(index);
                if (item.compareTo(smallest) < 0)
                {
                    smallest = item;
                    smallestPosition = index;
                }
            }
            remove(smallestPosition);
        }

      return smallest;
    }

	public boolean add(T newEntry) // OutOfMemoryError possible
	{
		Node newNode = new Node(newEntry);

		if (isEmpty())
			firstNode = newNode;
		else // add to end of nonempty list
		{
			Node lastNode = getNodeAt(length);
			lastNode.next = newNode; // make last node reference new node
		} // end if

		length++;
		return true;
	} // end add

	public boolean add(int newPosition, T newEntry) // OutOfMemoryError possible
	{
		boolean isSuccessful = true;

		if ((newPosition >= 1) && (newPosition <= length + 1)) {
			Node newNode = new Node(newEntry);

			if (isEmpty() || (newPosition == 1)) // case 1: add to beginning of
													// list
			{
				newNode.next = firstNode;
				firstNode = newNode;
			} else // case 2: list is not empty and newPosition > 1
			{
				Node nodeBefore = getNodeAt(newPosition - 1);
				Node nodeAfter = nodeBefore.next;
				newNode.next = nodeAfter;
				nodeBefore.next = newNode;
			} // end if

			length++;
		} else
			isSuccessful = false;

		return isSuccessful;
	} // end add

	public T remove(int givenPosition) {
		T result = null; // return value

		if ((givenPosition >= 1) && (givenPosition <= length)) {
			assert !isEmpty();

			if (givenPosition == 1) // case 1: remove first entry
			{
				result = firstNode.data; // save entry to be removed
				firstNode = firstNode.next;
			} else // case 2: givenPosition > 1
			{
				Node nodeBefore = getNodeAt(givenPosition - 1);
				Node nodeToRemove = nodeBefore.next;
				Node nodeAfter = nodeToRemove.next;
				nodeBefore.next = nodeAfter; // disconnect the node to be
												// removed
				result = nodeToRemove.data; // save entry to be removed
			} // end if

			length--;
		} // end if

		return result; // return removed entry, or
						// null if operation fails
	} // end remove

	public boolean replace(int givenPosition, T newEntry) {
		boolean isSuccessful = true;

		if ((givenPosition >= 1) && (givenPosition <= length)) {
			assert !isEmpty();

			Node desiredNode = getNodeAt(givenPosition);
			desiredNode.data = newEntry;
		} else
			isSuccessful = false;

		return isSuccessful;
	} // end replace

	public T getEntry(int givenPosition) {
		T result = null; // result to return

		if ((givenPosition >= 1) && (givenPosition <= length)) {
			assert !isEmpty();
			result = getNodeAt(givenPosition).data;
		} // end if

		return result;
	} // end getEntry

	public boolean contains(T anEntry) {
		boolean found = false;
		Node currentNode = firstNode;

		while (!found && (currentNode != null)) {
			if (anEntry.equals(currentNode.data))
				found = true;
			else
				currentNode = currentNode.next;
		} // end while

		return found;
	} // end contains

	public int getLength() {
		return length;
	} // end getLength

	public boolean isEmpty() {
		boolean result;

		if (length == 0) // or getLength() == 0
		{
			assert firstNode == null;
			result = true;
		} else {
			assert firstNode != null;
			result = false;
		} // end if

		return result;
	} // end isEmpty

	public boolean isFull() {
		return false;
	} // end isFull

	public void display() {
		// iterative
		Node currentNode = firstNode;
		while (currentNode != null) {
			System.out.println(currentNode.data);
			currentNode = currentNode.next;
		} // end while

		// recursive
		// displayChain(firstNode);
		// System.out.println();
	} // end display

	private void displayChain(Node nodeOne) {
		if (nodeOne != null) {
			System.out.print(nodeOne.data + " ");
			displayChain(nodeOne.next);
		} // end if
	} // end displayChain

	/**
	 * Task: Returns a reference to the node at a given position. Precondition:
	 * List is not empty; 1 <= givenPosition <= length.
	 */
	private Node getNodeAt(int givenPosition) {
		assert !isEmpty() && (1 <= givenPosition) && (givenPosition <= length);
		Node currentNode = firstNode;

		// traverse the list to locate the desired node
		for (int counter = 1; counter < givenPosition; counter++)
			currentNode = currentNode.next;

		assert currentNode != null;
		return currentNode;
	} // end getNodeAt

	private class Node {
		private T data; // entry in list
		private Node next; // link to next node

		private Node(T dataPortion) {
			data = dataPortion;
			next = null;
		} // end constructor

		private Node(T dataPortion, Node nextNode) {
			data = dataPortion;
			next = nextNode;
		} // end constructor
	} // end Node
} // end LList

