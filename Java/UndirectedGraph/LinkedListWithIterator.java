import java.util.Iterator;
import java.util.NoSuchElementException;
/**
 * A class that implements the ADT list by using a chain of nodes.
 * The list has an iterator. The class is based on LList.
 * 
 * @author Frank M. Carrano
 * @version 2.0
 */
public class LinkedListWithIterator<T>
             implements ListWithIteratorInterface<T>
{
	private Node firstNode; // reference to first node
	private int  length;  	// number of entries in list
  
	public LinkedListWithIterator()
	{
		clear();
	} // end default constructor

	public final void clear() // NOTICE clear cannot be final in interface
	{
		firstNode = null;
		length = 0;
	} // end clear
  
	public boolean add(T newEntry) 	      // OutOfMemoryError possible
	{
		Node newNode = new Node(newEntry);

		if (isEmpty())
			firstNode = newNode;
		else                                // add to end of nonempty list
		{
			Node lastNode = getNodeAt(length);
			lastNode.next = newNode;		      // make last node reference new node
		} // end if	
		
		length++;
		return true;
	}  // end add

  public boolean add(int newPosition, T newEntry) // OutOfMemoryError possible	                                                 
	{
		boolean isSuccessful = true;

		if ((newPosition >= 1) && (newPosition <= length+1)) 
		{	
			Node newNode = new Node(newEntry); 

			if (isEmpty() || (newPosition == 1))	      // case 1: add to beginning of list
			{
				newNode.next = firstNode;							
				firstNode = newNode;
			}
			else									                      // case 2: list is not empty and newPosition > 1
			{
				Node nodeBefore = getNodeAt(newPosition - 1);
				Node nodeAfter = nodeBefore.next;
				newNode.next = nodeAfter;
				nodeBefore.next = newNode;
			} // end if	
		
			length++;
		}
		else
			isSuccessful = false;
			
		return isSuccessful;
	} // end add

	public T remove(int givenPosition)
	{
	  T result = null;                 // return value
	  
	  if ((givenPosition >= 1) && (givenPosition <= length))
	  {
	    assert !isEmpty();
	    
	    if (givenPosition == 1)        // case 1: remove first entry
	    {
	      result = firstNode.data;     // save entry to be removed 
	      firstNode = firstNode.next;
	    }
	    else                           // case 2: givenPosition > 1
	    {
	      Node nodeBefore = getNodeAt(givenPosition - 1);
	      Node nodeToRemove = nodeBefore.next;
	      Node nodeAfter = nodeToRemove.next;
	      nodeBefore.next = nodeAfter; // disconnect the node to be removed
	      result = nodeToRemove.data;  // save entry to be removed
	    } // end if
	    
	    length--;
	  } // end if
	  
	  return result;                   // return removed entry, or 
	                                   // null if operation fails
	} // end remove

	public boolean replace(int givenPosition, T newEntry)
	{
		boolean isSuccessful = true;

    if ((givenPosition >= 1) && (givenPosition <= length))
    {   
    	assert !isEmpty();

			Node desiredNode = getNodeAt(givenPosition);
			desiredNode.data = newEntry;
    }    
		else
			isSuccessful = false;
			
		return isSuccessful;
  } // end replace

  public T getEntry(int givenPosition)
  {
  	T result = null;  // result to return
      
		if ((givenPosition >= 1) && (givenPosition <= length))
		{
			assert !isEmpty();
      result = getNodeAt(givenPosition).data;
   	} // end if
      
    return result;
  } // end getEntry

	public boolean contains(T anEntry)
	{
		boolean found = false;
		Node currentNode = firstNode;
		
		while (!found && (currentNode != null))
		{
			if (anEntry.equals(currentNode.data))
				found = true;
			else
				currentNode = currentNode.next;
		} // end while
		
		return found;
	} // end contains

  public int getLength()
  {
     return length;
  } // end getLength

  public boolean isEmpty()
  {
  	boolean result;
 		
   	if (length == 0) // or getLength() == 0
   	{
   		assert firstNode == null;
   		result = true;
   	}
   	else
   	{
   		assert firstNode != null;
   		result = false;
   	} // end if
   	
   	return result;
  } // end isEmpty
	
  public boolean isFull()
  {
     return false;
  } // end isFull

	public Iterator<T> getIterator()
	{
	  return new IteratorForLinkedList();
	} // end getIterator

  public Iterator<T> iterator()
  {
    return getIterator();
  } // end iterator

  public void display()
  {
	  // iterative
	  Node currentNode = firstNode;
		while (currentNode != null)
		{ 
			System.out.println(currentNode.data);
		  currentNode = currentNode.next; 
		} // end while  

		// recursive
//	displayChain(firstNode);
//	System.out.println();
  } // end display

  private void displayChain(Node nodeOne) 
	{ 
		if (nodeOne != null)
		{
			System.out.print(nodeOne.data + " ");
			displayChain(nodeOne.next);
		} // end if
	} // end displayChain

	/** Task: Returns a reference to the node at a given position.
	 *  Precondition: List is not empty; 1 <= givenPosition <= length. */
	private Node getNodeAt(int givenPosition)
	{
		assert !isEmpty() && (1 <= givenPosition) && (givenPosition <= length);
		Node currentNode = firstNode;
		
    // traverse the list to locate the desired node
		for (int counter = 1; counter < givenPosition; counter++)
			currentNode = currentNode.next;
		
		assert currentNode != null;
		return currentNode;
	} // end getNodeAt

//==================================

	private class IteratorForLinkedList implements Iterator<T>
	{
  	private Node nextNode;  // node containing next entry in iteration

		private IteratorForLinkedList()
		{
			nextNode = firstNode;
		} // end default constructor
		
		public boolean hasNext()
		{
			return nextNode != null;
		} // end hasNext

		public T next()
		{
			if (hasNext())
			{
				Node returnNode = nextNode; // get next node
				nextNode = nextNode.next;   // advance iterator
				
				return returnNode.data;     // return next entry in iteration
			}
			else
				throw new NoSuchElementException("Illegal call to next();" +
		                                     "iterator is after end of list.");
		} // end next

		public void remove()
		{
			throw new UnsupportedOperationException("remove() is not " +
		                                         	"supported by this iterator");
		} // end remove
	} // end IteratorForLinkedList
	
	private class Node 
	{
	  private T    data; // entry in list
	  private Node next; // link to next node

		private Node(T dataPortion)
		{
			data = dataPortion;
			next = null;	
		} // end constructor
		
		private Node(T dataPortion, Node nextNode)
		{
			data = dataPortion;
			next = nextNode;	
		} // end constructor
	} // end Node
} // end LinkedListWithIterator



