import java.util.Iterator;
import java.util.Stack;
import java.util.Queue;
import java.util.concurrent.LinkedBlockingQueue;
import java.util.PriorityQueue;

/**
 * A class that implements the ADT directed graph.
 * 
 * @author Frank M. Carrano
 * @version 2.0
 */
public class DirectedGraph<T> implements BasicGraphInterface <T>, java.io.Serializable {
	private DictionaryInterface<T, VertexInterface<T>> vertices;
	private int edgeCount;

	public DirectedGraph() {
		vertices = new LinkedDictionary<T, VertexInterface<T>>();
		edgeCount = 0;
	} // end default constructor

	public boolean addVertex(T vertexLabel) {
		VertexInterface<T> isDuplicate = vertices.add(vertexLabel, new Vertex(
				vertexLabel));
		return isDuplicate == null; // was add to dictionary successful?
	} // end addVertex

	public boolean addEdge(T begin, T end, double edgeWeight) {
		boolean result = false;

		VertexInterface<T> beginVertex = vertices.getValue(begin);
		VertexInterface<T> endVertex = vertices.getValue(end);

		if ((beginVertex != null) && (endVertex != null))
			result = beginVertex.connect(endVertex, edgeWeight);

		if (result)
			edgeCount++;

		return result;
	} // end addEdge

	public boolean addEdge(T begin, T end) {
		return addEdge(begin, end, 0);
	} // end addEdge

	public boolean hasEdge(T begin, T end) {
		boolean found = false;

		VertexInterface<T> beginVertex = vertices.getValue(begin);
		VertexInterface<T> endVertex = vertices.getValue(end);

		if ((beginVertex != null) && (endVertex != null)) {
			Iterator<VertexInterface<T>> neighbors = beginVertex
					.getNeighborIterator();
			while (!found && neighbors.hasNext()) {
				VertexInterface<T> nextNeighbor = neighbors.next();
				if (endVertex.equals(nextNeighbor))
					found = true;
			} // end while
		} // end if

		return found;
	} // end hasEdge

	public boolean isEmpty() {
		return vertices.isEmpty();
	} // end isEmpty

	public void clear() {
		vertices.clear();
		edgeCount = 0;
	} // end clear

	public int getNumberOfVertices() {
		return vertices.getSize();
	} // end getNumberOfVertices

	public int getNumberOfEdges() {
		return edgeCount;
	} // end getNumberOfEdges

	protected void resetVertices() {
		Iterator<VertexInterface<T>> vertexIterator = vertices
				.getValueIterator();
		while (vertexIterator.hasNext()) {
			VertexInterface<T> nextVertex = vertexIterator.next();
			nextVertex.unvisit();
			nextVertex.setCost(0);
			nextVertex.setPredecessor(null);
		} // end while
	} // end resetVertices

	public Queue<T> getBreadthFirstTraversal(T origin) {
		resetVertices();
		Queue<T> traversalOrder = new LinkedBlockingQueue<T>();
		Queue<VertexInterface<T>> vertexQueue = new LinkedBlockingQueue<VertexInterface<T>>();
		VertexInterface<T> originVertex = vertices.getValue(origin);
		originVertex.visit();
		traversalOrder.add(origin); // enqueue vertex label
		vertexQueue.add(originVertex); // enqueue vertex

		while (!vertexQueue.isEmpty()) {
			VertexInterface<T> frontVertex = vertexQueue.remove();

			Iterator<VertexInterface<T>> neighbors = frontVertex.getNeighborIterator();
			while (neighbors.hasNext()) {
				VertexInterface<T> nextNeighbor = neighbors.next();
				if (!nextNeighbor.isVisited()) {
					nextNeighbor.visit();
					traversalOrder.add(nextNeighbor.getLabel());
					vertexQueue.add(nextNeighbor);
				} // end if
			} // end while
		} // end while

		return traversalOrder;
	} // end getBreadthFirstTraversal

	public Queue<T> getDepthFirstTraversal(T origin) {
		// assumes graph is not empty
		resetVertices();
		Queue<T> traversalOrder = new LinkedBlockingQueue<T>();
		Stack<VertexInterface<T>> vertexStack = new Stack<VertexInterface<T>>();

		VertexInterface<T> originVertex = vertices.getValue(origin);
		originVertex.visit();
		traversalOrder.add(origin); // enqueue vertex label
		vertexStack.push(originVertex); // enqueue vertex

		while (!vertexStack.isEmpty()) {
			VertexInterface<T> topVertex = vertexStack.peek();
			VertexInterface<T> nextNeighbor = topVertex.getUnvisitedNeighbor();

			if (nextNeighbor != null) {
				nextNeighbor.visit();
				traversalOrder.add(nextNeighbor.getLabel());
				vertexStack.push(nextNeighbor);
			} else
				// all neighbors are visited
				vertexStack.pop();
		} // end while

		return traversalOrder;
	} // end getDepthFirstTraversal

	public Stack<T> getTopologicalOrder() {
		resetVertices();

		Stack<T> vertexStack = new Stack<T>();
		int numberOfVertices = getNumberOfVertices();
		for (int counter = 1; counter <= numberOfVertices; counter++) {
			VertexInterface<T> nextVertex = findTerminal();
			nextVertex.visit();
			vertexStack.push(nextVertex.getLabel());
		} // end for

		return vertexStack;
	} // end getTopologicalOrder

	

	

	protected VertexInterface<T> findTerminal() {
		boolean found = false;
		VertexInterface<T> result = null;

		Iterator<VertexInterface<T>> vertexIterator = vertices
				.getValueIterator();

		while (!found && vertexIterator.hasNext()) {
			VertexInterface<T> nextVertex = vertexIterator.next();

			// if nextVertex is unvisited AND has only visited neighbors)
			if (!nextVertex.isVisited()) {
				if (nextVertex.getUnvisitedNeighbor() == null) {
					found = true;
					result = nextVertex;
				} // end if
			} // end if
		} // end while

		return result;
	} // end findTerminal

	// Used for testing
	public void display() {
		System.out.println("Graph has " + getNumberOfVertices()
				+ " vertices and " + getNumberOfEdges() + " edges.");

		System.out.println("\nEdges exist from the first vertex in each line to the other vertices in the line.");
		System.out.println("(Edge weights are given; weights are zero for unweighted graphs):\n");
		Iterator<VertexInterface<T>> vertexIterator = vertices
				.getValueIterator();
		while (vertexIterator.hasNext()) {
			((Vertex<T>) (vertexIterator.next())).display();
		} // end while
	} // end display

	private class EntryPQ implements Comparable<EntryPQ>, java.io.Serializable {
		private VertexInterface<T> vertex;
		private VertexInterface<T> previousVertex;
		private double cost; // cost to nextVertex

		private EntryPQ(VertexInterface<T> vertex, double cost,
				VertexInterface<T> previousVertex) {
			this.vertex = vertex;
			this.previousVertex = previousVertex;
			this.cost = cost;
		} // end constructor

		public VertexInterface<T> getVertex() {
			return vertex;
		} // end getVertex

		public VertexInterface<T> getPredecessor() {
			return previousVertex;
		} // end getPredecessor

		public double getCost() {
			return cost;
		} // end getCost

		public int compareTo(EntryPQ otherEntry) {
			// using opposite of reality since our priority queue uses a
			// maxHeap;
			// could revise using a minheap
			return (int) Math.signum(otherEntry.cost - cost);
		} // end compareTo

		public String toString() {
			return vertex.toString() + " " + cost;
		} // end toString
	} // end EntryPQ
} // end DirectedGraph