/**
 * This interface describes a queue of unique entries (duplicates are not allowed).
 */
public interface NoDupsDePrioritizeQueueInterface <T> extends QueueInterface<T> {

	/*
	 * Task: Moves the given entry to the back of the queue. If the entry is not
	 * in the queue, just add it at the end.
	 * 
	 * @param entry the item to move or add
	 */
	public void moveToBack(T entry);
	
	/*
	 * * Task: displays the contents of the queue (to be used for testing);
	 * specifies the front and back of the queue
	 */
	public void display();
}
