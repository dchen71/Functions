/** * A class that implements the ADT stack by using a chain of nodes. * * @author Frank M. Carrano * @version 2.0 */public class LinkedStack<T> implements StackInterface<T>, java.io.Serializable {	private Node topNode; // references the first node in the chain	public LinkedStack() {		topNode = null;	}	public void push(T newEntry) {		Node newNode = new Node(newEntry, topNode);		topNode = newNode;	}	public T peek() {		T top = null;		if (topNode != null)			top = topNode.data;		return top;	}	public T peek2() {		T top2 = null;
        Node peekaboo = topNode;

        if(isEmpty())
            return null;
        else if(topNode.next == null)
            return null;

		if(topNode.next != null)
            top2 = topNode.next.data;
		return top2;	}	public T pop() {		T top = peek();		if (topNode != null)			topNode = topNode.next;		return top;	}	public void display() {		Node current = topNode;		System.out.print("Top: ");		while (current != null) {			System.out.print(current.data + " ");			current = current.next;		}		System.out.println();	}	public boolean isEmpty() {		return topNode == null;	}	public void clear() {		topNode = null;	}	private class Node implements java.io.Serializable {		private T data; // entry in stack		private Node next; // link to next node		private Node(T dataPortion) {			data = dataPortion;			next = null;		}		private Node(T dataPortion, Node linkPortion) {			data = dataPortion;			next = linkPortion;		}	}}
