
public interface NoDupsPrioritizeStackInterface<T> extends StackInterface<T> {

	/*
	 * Task: Moves the given entry to the top of the stack. If the entry is not
	 * in the stack, just add it at the top.
	 * 
	 * @param entry the item to move or add
	 */
	public void moveToTop(T entry);
	
	/*
	 * * Task: displays the contents of the stack (to be used for testing);
	 * specifies the top and bottom of the stack
	 */
	public void display();
}
