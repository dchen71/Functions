public class NoDupsDePrioritizeArrayQueue<T> implements NoDupsDePrioritizeQueueInterface<T>
{
	private T[] queue; // circular array of queue entries and one unused location
	private int frontIndex;
	private int backIndex;
	private static final int DEFAULT_INITIAL_CAPACITY = 10;

	public NoDupsDePrioritizeArrayQueue() {
		this(DEFAULT_INITIAL_CAPACITY);
	}

	public NoDupsDePrioritizeArrayQueue(int initialCapacity) {
		queue = (T[]) new Object[initialCapacity + 1];
		frontIndex = 0;
		backIndex = initialCapacity;
	}


	public void enqueue(T newEntry) {
		if (isArrayFull())
			doubleArray();

        if(isEmpty())
        {
            backIndex = (backIndex + 1) % queue.length;
            queue[backIndex] = newEntry;
        }
        else
        {
            boolean found = false;

            if(frontIndex < backIndex)
            {
                for(int start = frontIndex; start <= backIndex; start++)
                {
                    if(queue[start].equals(newEntry))
                    {
                        found = true;
                        break;
                    }
                }

                if(found == false)
                {
                        backIndex = (backIndex + 1) % queue.length;
                        queue[backIndex] = newEntry;
                }
            }
            else if(frontIndex == backIndex)
            {
                if(!queue[frontIndex].equals(newEntry))
                {
                    backIndex = (backIndex + 1) % queue.length;
                    queue[backIndex] = newEntry;
                }
            }
            else if(frontIndex > backIndex)
            {
                for(int start = frontIndex; start <= frontIndex; start++)
                {
                    if(queue[start].equals(newEntry))
                    {
                        found = true;
                        break;
                    }


                }

                for(int start = 0; start <= backIndex; start++)
                {
                    if(!found)
                    {
                        if(queue[start].equals(newEntry))
                        {
                            found = true;
                            break;
                        }
                    }
                    else
                        break;
                }

                if(found == false)
                {
                    backIndex = (backIndex + 1) % queue.length;
                    queue[backIndex] = newEntry;
                }
            }
        }

	}

	public T getFront() {
		T front = null;

		if (!isEmpty())
			front = queue[frontIndex];

		return front;
	}

	public T dequeue() {
		T front = null;

		if (!isEmpty()) {
			front = queue[frontIndex];
			queue[frontIndex] = null;
			frontIndex = (frontIndex + 1) % queue.length;
		}

		return front;
	}


	public boolean isEmpty() {
		return frontIndex == ((backIndex + 1) % queue.length);
	}


	public void clear() {
		if (!isEmpty()) { // deallocates only the used portion
			for (int index = frontIndex; index != backIndex; index = (index + 1)
					% queue.length) {
				queue[index] = null;
			}

			queue[backIndex] = null;
		}

		frontIndex = 0;
		backIndex = queue.length - 1;
	}



	private boolean isArrayFull() {
		return frontIndex == ((backIndex + 2) % queue.length);
	}


	private void doubleArray() {
		T[] oldQueue = queue;
		int oldSize = oldQueue.length;

		queue = (T[]) new Object[2 * oldSize];

		for (int index = 0; index < oldSize - 1; index++) {
			queue[index] = oldQueue[frontIndex];
			frontIndex = (frontIndex + 1) % oldSize;
		}

		frontIndex = 0;
		backIndex = oldSize - 2;
	}


	public void moveToBack(T entry)
	{
        T temp = entry;

        if(!isEmpty())
        {
            if(frontIndex == backIndex)
            {
                if(!queue[frontIndex].equals(entry))
                    enqueue(entry);
            }
            else if(frontIndex < backIndex)
            {
                boolean found = false;
                int foundP = 0;

                for(int start = frontIndex; start <= backIndex; start++)
                {
                    if(queue[start].equals(entry))
                    {
                        found = true;
                        foundP = start;
                        break;
                    }
                }

                if(!found)
                    enqueue(entry);
                else
                {
                    for(int start = foundP; start < backIndex; start++)
                    {
                        queue[start] = queue[start + 1];
                    }

                    queue[backIndex] = temp;
                }
            }
            else if(frontIndex > backIndex)
            {
                int length = queue.length - 1;
                int counter = 0;

                int front = frontIndex;

                boolean found = false;
                int foundP = 0;

                for(int start = frontIndex; start <= length; start++)
                {
                    if(found == true)
                        break;
                    else
                    {
                        if(queue[start].equals(entry))
                        {
                            found = true;
                            foundP = start;
                            break;
                        }
                    }
                }

                for(int start = 0; start <= backIndex; start++)
                {
                    if(found == true)
                        break;
                    else
                    {
                        if(queue[start].equals(entry))
                        {
                            found = true;
                            foundP = start;
                            break;
                        }
                    }
                }

                if(found == false)
                {
                    enqueue(entry);
                }
                else
                {
                    if(foundP >= frontIndex)
                    {
                        for(int start = foundP; start < length; start++)
                        {
                            queue[start] = queue[start + 1];
                        }

                        for(int start = 0; start <= backIndex; start++)
                        {
                            queue[start] = queue[start + 1];
                        }

                        queue[backIndex] = temp;
                    }
                    else
                    {
                        for(int start = foundP; start < backIndex; start++)
                        {
                            queue[start] = queue[start + 1];
                        }

                        queue[backIndex] = temp;
                    }
                }
            }

        }
        else
        {
            enqueue(entry);
        }
	}


	public void display()
    {
        if(!isEmpty())
        {
            if(frontIndex == backIndex)
                System.out.println("Only entry: " + queue[frontIndex]);
            else if(frontIndex < backIndex)
            {
                for(int start = frontIndex; start <= backIndex; start++)
                {
                    if(start == frontIndex)
                        System.out.println("Front: " + queue[start]);
                    else if(start > frontIndex  && start != backIndex)
                        System.out.println("Middle: " + queue[start]);
                    else if(start == backIndex)
                        System.out.println("Back: " + queue[start]);
                }
            }
            else if(frontIndex > backIndex)
            {
                int length = queue.length - 1;

                for(int start = frontIndex; start <= length; start++)
                {
                    if(start == frontIndex)
                        System.out.println("Front: " + queue[start]);
                    else
                        System.out.println("Middle: " + queue[start]);
                }

                for(int start = 0; start <= backIndex; start++)
                {
                    if(start != backIndex)
                        System.out.println("Middle: " + queue[start]);
                    else
                        System.out.println("End: " + queue[start]);
                }
            }

        }
        else
        {
            System.out.println("Empty!");
        }
    }
}
