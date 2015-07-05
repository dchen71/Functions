public class Stack<T> implements StackInterface<T>, java.io.Serializable
{
  private DequeInterface deque;

	public HW9_Stack()
	{
		deque = new LinkedDeque();
	}

    public void push(T newEntry)
    {
        deque.addToBack(newEntry);
    }

    public T pop()
    {
        return (T)deque.removeBack();
    }

    public T peek()
    {
        return (T)deque.getBack();
    }

    public boolean isEmpty()
    {
        return deque.isEmpty();
    }

    public void clear()
    {
        deque.clear();
    }
}
