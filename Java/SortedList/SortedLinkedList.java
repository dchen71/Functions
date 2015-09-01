public class SortedLinkedList<T extends Comparable<? super T>>
    public int getPosition(T anEntry)
    {
        return 0;
    }

    public boolean remove(T anEntry)
    {
        return false;
    }

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


	public T getEntry(int givenPosition) {
		T result = null; // result to return

		if ((givenPosition >= 1) && (givenPosition <= length)) {
			assert !isEmpty();
			result = getNodeAt(givenPosition).data;
		} // end if

		return result;
	} // end getEntry

    public boolean contains(T anEntry)
    {
		Node currentNode = firstNode;

		if(currentNode != null)
        {
            if(length > 0)
            {
                boolean found = false;

                while (!found && (currentNode != null))
                {
                    if (anEntry.equals(currentNode.data))
                        found = true;
                    else if(currentNode.next != null && anEntry.compareTo(currentNode.data) > 0 && anEntry.compareTo(currentNode.next.data) < 0)
                    {
                        found = false;
                        break;
                    }
                    else
                        currentNode = currentNode.next;
                }

                return found;
            }
            else
                return false;
        }
        else
            return false;
    }


   public void merge(SortedListInterface<T> sList)
    {
        int adder = 1;

        if(!isEmpty())
        {
            if(sList.isEmpty() != false)
            {
                addN(sList);
            }
        }
        else
        {
            if(sList.isEmpty() != true)
            {
                clear();

                while(adder <= sList.getLength())
                {
                    add(sList.getEntry(adder));
                    length++;
                    adder++;
                }
            }
        }
    }

    private void addN(SortedListInterface<T> sList)
    {
        Node currentList = firstNode;
        Node addable = new Node(sList.getEntry(length + 1));

        clear();

        int pointer = 0;

        while(currentList != null && addable != null)
        {
            addable = new Node(sList.getEntry(pointer + 1));
            if(currentList != null)
            {
                if(addable!= null)
                {
                    if(currentList.data.compareTo(addable.data) == 0)
                    {
                        Node lastNode = getNodeAt(length);
                        lastNode.next = currentList;
                        lastNode.next.next = addable;
                        currentList = currentList.next;
                        length += 1;
                        pointer += 1;
                    }
                    else if(currentList.data.compareTo(addable.data) < 0)
                    {
                        Node lastNode = getNodeAt(length);
                        lastNode.next = currentList;
                        currentList = currentList.next;
                        length += 1;
                    }
                    else
                    {
                        Node lastNode = getNodeAt(length);
                        lastNode.next = addable;
                        length += 1;
                        pointer += 1;
                    }
                }
            }
            else
            {
                if(addable!= null)
                {
                    Node lastNode = getNodeAt(length);
                    lastNode.next = addable;
                    length += 1;
                    pointer += 1;
                }
            }
        }

    }

    private Node getNodeBefore(T anEntry)
    public void display()
    {
		Node currentNode = firstNode;
		while (currentNode != null) {
			System.out.println(currentNode.data);
			currentNode = currentNode.next;
		}
    }

    public int getLength()
    {
        return length;
    }

    public boolean isFull()
    {
        return false;
    }

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

	public final void clear() // NOTICE clear cannot be final in interface
	{
		firstNode = null;
		length = 0;
	} // end clear

	private Node getNodeAt(int givenPosition) {
		assert !isEmpty() && (1 <= givenPosition) && (givenPosition <= length);
		Node currentNode = firstNode;

		// traverse the list to locate the desired node
		for (int counter = 1; counter < givenPosition; counter++)
			currentNode = currentNode.next;

		assert currentNode != null;
		return currentNode;
	} // end getNodeAt



			data = dataPortion;
			next = null;
		} // end constructor

		private Node(T dataPortion, Node nextNode) {
			data = dataPortion;
			next = nextNode;
		} // end constructor

        {
            return data;
        }
        private void setData(T entry)
        {
            this.data = data;
        }
        private Node getNextNode()
        {
            return next;
        }
        private void setNextNode(Node next)
        {
           this.next = next;
        }