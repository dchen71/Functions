import java.util.Iterator;
import java.util.NoSuchElementException;
import java.io.Serializable;

/**
 * A class that implements the ADT dictionary by using a chain of nodes.
 * The dictionary is not sorted and has distinct search keys.
 *
 * @author Frank M. Carrano
 * @version 2.0
 */
public class LinkedDictionary<K, V> 
             implements DictionaryInterface<K, V>, Serializable
{
	private Node firstNode;   // reference to first node of chain
	private int  currentSize; // number of entries 
	
	public LinkedDictionary()
	{
		firstNode = null;		
    currentSize = 0;
	} // end default constructor
	
	// 18.25
  public V add(K key, V value)
  {
    V result = null;
    
    // search chain for a node containing key
    Node currentNode = firstNode;
    while ( (currentNode != null) && !key.equals(currentNode.getKey()) )
    {
      currentNode = currentNode.getNextNode();
    } // end while
    
    if (currentNode == null)
    {
    	// key not in dictionary; add new node at beginning of chain
      Node newNode = new Node(key, value);
      newNode.setNextNode(firstNode);
      firstNode = newNode;
      currentSize++;
    }
    else
    {
    	// key in dictionary; replace corresponding value
      result = currentNode.getValue();
      currentNode.setValue(value); // replace value
    } // end if
    
    return result;
  } // end add

  public V remove(K key)
	{
   	V result = null;  // return value
   	
		if (!isEmpty())
		{	
    	// search chain for a node containing key;
	    // save reference to preceding node
			Node currentNode = firstNode;
			Node nodeBefore = null;
			
    	while ( (currentNode != null) && !key.equals(currentNode.getKey()) )
			{
				nodeBefore = currentNode;
				currentNode = currentNode.getNextNode();
			} // end while
			
			if (currentNode != null)
			{
				// node found; remove it
				Node nodeAfter = currentNode.getNextNode(); // node after the one to be removed

				if (nodeBefore == null)
					firstNode = nodeAfter;
				else
					nodeBefore.setNextNode(nodeAfter);        // disconnect the node to be removed

				result = currentNode.getValue();            // get ready to return removed entry
			  currentSize--;                              // decrease length for both cases
			} // end if
		} // end if
			
    return result;  
  } // end remove

  public V getValue(K key)
  {
  	V result = null;

    // find node before the one that contains or could contain key
		Node currentNode = firstNode;
		
    while ( (currentNode != null) && !key.equals(currentNode.getKey()) )
		{
			currentNode = currentNode.getNextNode();
		} // end while

		if (currentNode != null)
		{
			result = currentNode.getValue();
		} // end if
		
		return result;
  } // end getValue

	public boolean contains(K key)
  {
   	return getValue(key) != null; 
  } // end contains

  public boolean isEmpty()
  {
    return currentSize == 0;
  } // end isEmpty
	
  public boolean isFull()
  {
    return false;
  } // end isFull

  public int getSize()
  {
    return currentSize;
  } // end getSize

	public final void clear()
	{ 
		firstNode = null;		
    currentSize = 0;
  } // end clear

	public Iterator<K> getKeyIterator()
	{
		return new KeyIterator();
	} // end getKeyIterator
	
	public Iterator<V> getValueIterator()
	{
		return new ValueIterator();
	} // end getValueIterator

  // 18.26
	private class KeyIterator implements Iterator<K>
	{
		private Node nextNode;
		
		private KeyIterator()
		{
			nextNode = firstNode;
		} // end default constructor
		
		public boolean hasNext() 
		{
			return nextNode != null;
		} // end hasNext
		
		public K next()
		{
			K result;// = null; // null not used or needed here
			
			if (hasNext())
			{
				result = nextNode.getKey();
				nextNode = nextNode.getNextNode();
			}
			else
			{
				throw new NoSuchElementException();
			} // end if
		
			return result;
		} // end next
		
		public void remove()
		{
			throw new UnsupportedOperationException();
		} // end remove
	} // end KeyIterator 
	
	private class ValueIterator implements Iterator<V>
	{
		private Node nextNode;
		
		private ValueIterator()
		{
			nextNode = firstNode;
		} // end default constructor
		
		public boolean hasNext() 
		{
			return nextNode != null;
		} // end hasNext
		
		public V next()
		{
			V result;
			
			if (hasNext())
			{
				result = nextNode.getValue();
				nextNode = nextNode.getNextNode();
			}
			else
			{
				throw new NoSuchElementException();
			} // end if
		
			return result;
		} // end next
		
		public void remove()
		{
			throw new java.lang.UnsupportedOperationException();
		} // end remove
	} // end getValueIterator

	private class Node implements Serializable
	{
		private K key;
		private V value;
		private Node next;

		private Node(K searchKey, V dataValue)
		{
			key = searchKey;
			value = dataValue;
			next = null;	
		} // end constructor
		
		private Node(K searchKey, V dataValue, Node nextNode)
		{
			key = searchKey;
			value = dataValue;
			next = nextNode;	
		} // end constructor
		
		private K getKey()
		{
			return key;
		} // end getKey
		
		private V getValue()
		{
			return value;
		} // end getValue

		private void setValue(V newValue)
		{
			value = newValue;
		} // end setValue

		private Node getNextNode()
		{
			return next;
		} // end getNextNode
		
		private void setNextNode(Node nextNode)
		{
			next = nextNode;
		} // end setNextNode
	} // end Node
} // end LinkedDictionary
		
