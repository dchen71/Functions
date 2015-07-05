public class NoDupsPrioritizeArrayStack<T> implements NoDupsPrioritizeStackInterface<T>
{
	private T[] stack; // array of stack entries
	private int topIndex; // index of top entry
	private static final int DEFAULT_INITIAL_CAPACITY = 50;


	public NoDupsPrioritizeArrayStack() {
		this(DEFAULT_INITIAL_CAPACITY);
	}

	public NoDupsPrioritizeArrayStack(int initialCapacity) {
		stack = (T[]) new Object[initialCapacity];
		topIndex = -1;
	}

	public void push(T newEntry) {
		boolean xist = false;

        if(!isEmpty())
        {
            for(int start = 0; start <= topIndex; start++)
            {
                if(stack[start].equals(newEntry))
                {
                    xist = true;
                    break;
                }
            }
        }


        if(xist == false)
        {
            topIndex++;

            if (topIndex >= stack.length) // if array is full,
                doubleArray(); // expand array

            stack[topIndex] = newEntry;
        }

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

	public void moveToTop(T entry)
	{
        if(!isEmpty())
        {
            for(int start = 0; start <= topIndex; start++)
            {
                if(stack[start].equals(entry))
                {
                    if (topIndex >= stack.length) // if array is full,
                        doubleArray(); // expand array

                    stack[topIndex + 1] = stack[start];

                    for(int begin = start; begin <= topIndex; begin++)
                    {
                        stack[begin] = stack[begin + 1];
                    }

                    break;
                }
                else if(start == topIndex)
                {
                    push(entry);
                }
            }
        }
        else
        {
            push(entry);
        }

	}


	public void display()
	{
	    if(!isEmpty())
        {
            for(int start = 0; start <= topIndex; start++)
            {
                if(start == 0)
                    System.out.println("Bottom: " + stack[start]);
                else if(start > 0  && start != topIndex)
                    System.out.println("Middle: " + stack[start]);
                else if(start == topIndex)
                    System.out.println("Top: " + stack[start]);
            }
        }
        else
        {
            System.out.println("Empty!");
        }
	}
}
