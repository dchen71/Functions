

/**
 * An interface for the ADT sorted list.
 * Entries in the list have positions that begin with 1.
 * 
 * @author Frank M. Carrano
 * @version 2.0
 */
public interface SortedListInterface<T extends Comparable<? super T>>
{
  /** Task: Adds a new entry to the sorted list in its proper order.
   *  @param newEntry  the object to be added as a new entry
   *  @return true if the addition is successful */
  public boolean add(T newEntry);
  
  /** Task: Removes a specified entry from the sorted list.
   *  @param anEntry  the object to be removed
   *  @return true if anEntry was located and removed */
  public boolean remove(T anEntry);
  
  /** Task: Gets the position of an entry in the sorted list.
   *  @param anEntry  the object to be found
   *  @return the position of the first or only occurrence of anEntry 
   *          if it occurs in the list; otherwise returns the position 
   *          where anEntry would occur in the list, but as a negative 
   *          integer */
  public int getPosition(T anEntry);
  
  // The following methods are described in Segment 4.10 of Chapter 4 
  // as part of the ADT list:
  
  public T getEntry(int givenPosition);
  public boolean contains(T anEntry);
  public T remove(int givenPosition);
  public void clear();
  public int getLength();
  public boolean isEmpty();
  public boolean isFull();
  public void display();
} // end SortedListInterface
