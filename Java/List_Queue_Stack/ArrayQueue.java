/**

import static java.lang.Math.abs;

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
