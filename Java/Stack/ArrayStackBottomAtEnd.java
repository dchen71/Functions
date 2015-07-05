public class ArrayStackBottomAtEnd<T> implements StackInterface<T> {

	private T[] stack;
	private int topIndex;
	
	public final static int DEFAULT_INITIAL_CAPACITY = 50;

	public ArrayStackBottomAtEnd() {
		stack = (T[]) new Object[DEFAULT_INITIAL_CAPACITY];
		topIndex = stack.length;
	}

	public void push(T newEntry) {
		if(topIndex == 0) { // array is full 
			doubleCapacity(); // expand the array and copy the contents
		}
		
		topIndex--; // decrement topIndex to the new location of the top
		stack[topIndex] = newEntry; // push the element onto the stack
	}
	
	private void doubleCapacity() {
		int newSize = stack.length * 2;
		int oldSize = stack.length;
		T[] biggerStack = (T[]) new Object[newSize];
		
		for(int i=0; i<stack.length; i++) {
			biggerStack[oldSize + i] = stack[i];
		}
		stack = biggerStack;
	}
	

	public T pop() {
		T top = null;
		
		if(!isEmpty()) { // if the stack is not empty
			top = stack[topIndex]; // get the element on the top
			topIndex++; // and increment the topIndex to point to the new top
		}
		
		return top;
	}

	public T peek() {
		T top = null;
		
		if(!isEmpty() ) {
			top = stack[topIndex];
		}
		
		return top;

	}

	public boolean isEmpty() {
		return topIndex == stack.length;
	}

	public void clear() {
		
		for(int i = topIndex; i<stack.length; i++) {
			stack[i] = null;
			topIndex++;
		}
		topIndex = stack.length; 
	}


}
