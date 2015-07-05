/**
 * A class that implements the ADT stack by using an expandable array.
 * 
 */
public class ArrayStack<T> implements StackInterface<T> {
	
	private T[] stack; // array of stack entries
	private int topIndex; // index of top entry
	private static final int DEFAULT_INITIAL_CAPACITY = 50;

	public ArrayStack() {
		this(DEFAULT_INITIAL_CAPACITY);
	} 

	public ArrayStack(int initialCapacity) {
		stack = (T[]) new Object[initialCapacity];
		topIndex = -1;
	} 

	public void push(T newEntry) {
		topIndex++;

		if (topIndex >= stack.length) // if array is full,
			doubleArray(); // expand array

		stack[topIndex] = newEntry;
	}


	public T peek() {
		T top = null;

		if (!isEmpty())
			top = stack[topIndex];

		return top;
	} 


	public T pop() {
		T top = null;

		if (!isEmpty()) {
			top = stack[topIndex];
			stack[topIndex] = null;
			topIndex--;
		} 

		return top;
	} 
	
	public boolean isEmpty() {
		return topIndex < 0;
	} 


	public void clear() {
		for (; topIndex > -1; topIndex--)
			stack[topIndex] = null;
	} 
	


	private void doubleArray() {
		T[] oldStack = stack; // get reference to array of stack entries
		int oldSize = oldStack.length; // get max size of original array

		stack = (T[]) new Object[2 * oldSize]; // double size of array

		// copy entries from old array to new, bigger array
		System.arraycopy(oldStack, 0, stack, 0, oldSize);


	} 
} 