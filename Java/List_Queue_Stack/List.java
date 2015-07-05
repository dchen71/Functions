public class List<T> implements ListInterface<T>, java.io.Serializable
{
    private ListInterface array;
    private int intSize = 100;

	public HW9_List()
	{
		array = new AList(intSize);
	}

    public boolean add(T newEntry)
    {
        return array.add(newEntry);
    }

    public boolean add(int newPosition, T newEntry)
    {
        return add(newPosition, newEntry);
    }

    public T remove(int givenPosition)
    {
        return (T)array.remove(givenPosition);
    }

    public void clear()
    {
        array.clear();
    }

    public boolean replace(int givenPosition, T newEntry)
    {
        return array.replace(givenPosition, newEntry);
    }

    public T getEntry(int givenPosition)
    {
        return (T)array.getEntry(givenPosition);
    }

    public boolean contains(T anEntry)
    {
        return array.contains(anEntry);
    }

    public int getLength()
    {
        return array.getLength();
    }

    public void enqueue(T newEntry) //ENQUEUE
    {
        array.add(newEntry);
    }

	public T getFront() //GETFRONT
	{
		return (T)array.getEntry(1);
	}

	public T dequeue() //DEQUEUE
	{
        return (T)array.remove(1);
	}


    public boolean isEmpty()
    {
        return array.isEmpty();
    }

    public boolean isFull()
    {
        return array.isFull();
    }

    public void display()
    {
        array.display();
    }

}

