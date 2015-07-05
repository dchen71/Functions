import java.util.Iterator;

public class BSTSortedList<T extends Comparable<? super T>> implements SortedListInterface<T> {

	private BinarySearchTree<T> tree;

	public BSTSortedList()
	{
        super();
	}

	public BSTSortedList(T newEntry)
	{
        super();
	}

	public boolean add(T newEntry)
	{
		if(isEmpty())
            tree = new BinarySearchTree<T>(newEntry);
        else
            tree.add(newEntry);

		return true;
	}

	public boolean remove(T anEntry)
	{
        if(contains(anEntry))
        {
            tree.remove(anEntry);
            return true;
        }
        else
            return false;

	}

	public int getPosition(T anEntry)
	{
		int pos = 0;
        boolean found = false;

        Iterator<T> list = getInorderIterator();
        T first, second;
        second = anEntry;

        if(list.hasNext())
        {
            while(list.hasNext() && found == false)
            {
                first = list.next();
                pos++;

                if(first.compareTo(anEntry) == 0)
                    found = true;
                else if(first.compareTo(anEntry) < 0)
                {
                    if(second.compareTo(anEntry) > 0)
                    {
                        pos = -pos;
                        break;
                    }
                    else if(!list.hasNext())
                    {
                        pos = -pos - 1;
                        break;
                    }
                    else
                        second = first;
                }
                else if(first.compareTo(anEntry) > 0)
                {
                    if(second.compareTo(anEntry) < 0)
                    {
                        pos = -pos;
                        break;
                    }
                    else if(pos == 1)
                    {
                        pos = -pos;
                        break;
                    }
                    else
                        second = first;
                }
            }
        }
        else
            pos = 1;


		return pos;
	}

	public T getEntry(int givenPosition)
	{
		int pos = 1;

        Iterator<T> list = getInorderIterator();
        T entry = null;

        if(list.hasNext() && givenPosition <= getLength())
        {
            while(list.hasNext() && pos <= givenPosition)
            {
                entry = list.next();
                pos++;
            }
        }
        else
            entry = null;


		return entry;
	}

	public boolean contains(T anEntry)
	{
		return tree.contains(anEntry);
	}

	public T remove(int givenPosition)
	{
		T oldAns = null;
		if(givenPosition <= getLength())
        {
            oldAns = getEntry(givenPosition);
            tree.remove(oldAns);
        }

		return oldAns;
	}

	public void clear()
	{
        tree = null;
	}

	public int getLength()
	{
		return tree.getNumberOfNodes();
	}

	public boolean isEmpty()
	{
		if(tree!= null)
            return false;
        else
            return true;
	}

	public boolean isFull()
	{
		return false;
	}

	public void display()
	{
        tree.inorderTraverse();
	}

	public Iterator<T> getInorderIterator()
	{
		return tree.getInorderIterator();
	}
}
