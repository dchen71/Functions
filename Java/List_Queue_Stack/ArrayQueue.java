/** * A class that implements the ADT queue by using an expandable circular array * with one unused location. * * @author Frank M. Carrano * @version 2.0 */

import static java.lang.Math.abs;
public class ArrayQueue<T> implements QueueInterface<T>, java.io.Serializable {	private T[] queue; // circular array of queue entries and one unused						// location	private int frontIndex;	private int backIndex;	private static final int DEFAULT_INITIAL_CAPACITY = 50;	public ArrayQueue() {		this(DEFAULT_INITIAL_CAPACITY);	} // end default constructor	public ArrayQueue(int initialCapacity) {		queue = (T[]) new Object[initialCapacity + 1];		frontIndex = 0;		backIndex = initialCapacity;	} // end constructor	public void enqueue(T newEntry) {		if (isArrayFull()) // isArrayFull and			doubleArray(); // doubleArray are private		backIndex = (backIndex + 1) % queue.length;		queue[backIndex] = newEntry;	} // end enqueue	public T getFront() {		T front = null;		if (!isEmpty())			front = queue[frontIndex];		return front;	} // end getFront	public T dequeue() {		T front = null;		if (!isEmpty()) {			front = queue[frontIndex];			queue[frontIndex] = null;			frontIndex = (frontIndex + 1) % queue.length;		} // end if		return front;	} // end dequeue	public boolean isEmpty() {		return frontIndex == ((backIndex + 1) % queue.length);	} // end isEmpty	public void clear() {		if (!isEmpty()) { // deallocates only the used portion			for (int index = frontIndex; index != backIndex; index = (index + 1)					% queue.length) {				queue[index] = null;			} // end for			queue[backIndex] = null;		} // end if		frontIndex = 0;		backIndex = queue.length - 1;	} // end clear
    public void splice(QueueInterface<T> anotherQueue)
    {
        QueueInterface<T> copyQueue = anotherQueue;
        QueueInterface<T> fixQueue = new ArrayQueue();

        if(isEmpty())
        {
            while(!copyQueue.isEmpty())
            {
                fixQueue.enqueue(copyQueue.getFront());
                enqueue(copyQueue.dequeue());
            }
        }
        else if(!isEmpty())
        {
            while(!copyQueue.isEmpty())
            {
                fixQueue.enqueue(copyQueue.getFront());
                enqueue(copyQueue.dequeue());
            }
        }

        while(!fixQueue.isEmpty())
        {
            anotherQueue.enqueue(fixQueue.dequeue());
        }
    }

    public void splice(ArrayQueue anotherQueue)
    {
        T[] copyQueue = (T[])anotherQueue.getArray();
        int otherF = anotherQueue.getFIndex();
        int otherB = anotherQueue.getBIndex();
        int spacing = abs(otherF - otherB) + 1;
        int length = copyQueue.length - 1;

        if(isEmpty())
        {
            if(!anotherQueue.isEmpty())
            {
                while(spacing != 0)
                {
                    if(otherF == otherB && copyQueue[otherF] != null)
                    {
                        enqueue(copyQueue[otherF]);
                    }
                    else
                    {
                        if(otherF <= length || otherF <= otherB && copyQueue[otherF] != null)
                        {
                            enqueue(copyQueue[otherF]);
                            otherF++;
                        }
                        else if(otherB < otherF)
                        {
                            enqueue(copyQueue[otherB]);
                            otherB--;
                        }
                    }
                    spacing--;
                }
            }
        }
        else if(!isEmpty())
        {
            if(!anotherQueue.isEmpty())
            {
                while(spacing != 0)
                {
                    if(otherF == otherB && copyQueue[otherF] != null)
                    {
                        enqueue(copyQueue[otherF]);
                    }
                    else
                    {
                        if(otherF <= length || otherF <= otherB && copyQueue[otherF] != null)
                        {
                            enqueue(copyQueue[otherF]);
                            otherF++;
                        }
                        else if(otherB < otherF)
                        {
                            enqueue(copyQueue[otherB]);
                            otherB--;
                        }
                    }
                    spacing--;
                }
            }
        }


    }

    public T[] getArray()
    {
        return queue;
    }

    public int getFIndex()
    {
        return frontIndex;
    }

    public int getBIndex()
    {
        return backIndex;
    }
	private boolean isArrayFull() {		return frontIndex == ((backIndex + 2) % queue.length);	} // end isArrayFull	private void doubleArray() {		T[] oldQueue = queue;		int oldSize = oldQueue.length;		queue = (T[]) new Object[2 * oldSize];		for (int index = 0; index < oldSize - 1; index++) {			queue[index] = oldQueue[frontIndex];			frontIndex = (frontIndex + 1) % oldSize;		} // end for		frontIndex = 0;		backIndex = oldSize - 2;	} // end doubleArray} // end ArrayQueue
