public class EntryList<T> implements EntryWayListInterface<T>
{
	private Node firstNode; // reference to first node
	private int length; // number of entries in list

    public EntryList()
    {
        length = 0;

    }

    public EntryList(T[] items)
    {
        for(int start = 0; start < items.length; start++)
        {
            Node newNode = new Node(items[start]);

            if (isEmpty()) // case 1: add to beginning of
                                                    // list
            {
                newNode.next = firstNode;
                firstNode = newNode;
            }
            else // case 2: list is not empty and newPosition > 1
			{
				Node nodeBefore = getNodeAt(start);
				Node nodeAfter = nodeBefore.next;
				newNode.next = nodeAfter;
				nodeBefore.next = newNode;
			} // end if

                length++;
        }

    }

    public EntryList(T[] items, int numItem)
    {
        for(int start = 0; start < numItem; start++)
        {
            Node newNode = new Node(items[start]);

            if (isEmpty()) // case 1: add to beginning of
                                                    // list
            {
                newNode.next = firstNode;
                firstNode = newNode;
            }
            else // case 2: list is not empty and newPosition > 1
			{
				Node nodeBefore = getNodeAt(start);
				Node nodeAfter = nodeBefore.next;
				newNode.next = nodeAfter;
				nodeBefore.next = newNode;
			} // end if

                length++;
        }

    }

  /** Task: Adds a new entry to the first member of the list.
   *  @param newEntry - the object to be added as a new entry
   *  @return true if newEntry added to the head of the list otherwise false if unable to */
    public boolean insertHead(T newEntry)
    {
        boolean added = false;
        Node newNode = new Node(newEntry);

        newNode.next = firstNode;
        firstNode = newNode;

        length++;

        return added;
    }


  /** Task: Adds a new entry at the tail end of the list
   *  @param newEntry - the object to be added to the end of the list
   *  @return true if newEntry added to the tail end of the list otherwise false if unable to */
    public boolean insertTail(T newEntry)
    {
        boolean added = false;
        if(length == 0)
            insertHead(newEntry);
        else
        {
        Node newNode = new Node(newEntry);

        Node lastNode = getNodeAt(length);
        lastNode.next = newNode;

        length++;
        }


        return added;
    }


  /** Task: Deletes the 1st member of the list
  *   @return returns the object that you had deleted from the list */
    public T deleteHead()
    {
        T head = null;
        if (length > 0)
        {
            Node secNode = getNodeAt(2);
            head = getNodeAt(0).data;

            firstNode = secNode;

            length--;
        }
        else
        {
            head = null;
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

        tail = getNodeAt(length).data;
        Node secLastNode = getNodeAt(length - 1);

        secLastNode.next = null;

        length--;
        }
        else
        {
            tail = null;
        }


        return tail;
    }


  /** Task: Displays the entries in the list */
    public void display()
    {
		Node currentNode = firstNode;
		while (currentNode != null)
        {
			System.out.println(currentNode.data);
			currentNode = currentNode.next;
        }
    }


  /** Task: Sees whether the list contains a given entry.
   *  @param anEntry - the object that will be checked against the list
   *  @return returns position where anEntry was found */
    public int contains(T anEntry)
    {
		boolean found = false;
		int loc = 0;
		Node currentNode = firstNode;

		while (!found && (currentNode != null)) {
			if (anEntry.equals(currentNode.data))
				{
				    found = true;
				    loc+=1;
				}
			else
				{
				    currentNode = currentNode.next;
				    loc += 1;
				}
		} // end while

        if(found == false)
            loc =0;

		return loc;
    }


  /** Task: Checks if the list is empty
   *  @return true if list is empty, otherwise false */
    public boolean isEmpty()
    {
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
    }


  /** Task: Checks if the list is full
   *  @return true if list is full, otherwise false */
    public boolean isFull()
    {
        return false;
    }


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
}
