import java.util.Queue;


public class UndirectedGraph<T> implements BasicGraphInterface <T> {

	private DirectedGraph digraph;

	public UndirectedGraph() {
		digraph = new DirectedGraph();
	}

	public boolean addVertex(T vertexLabel) {
		return digraph.addVertex(vertexLabel);
	}

    public boolean addEdge(T begin, T end, double edgeWeight) {
		boolean result1 = false;
        boolean result2 = false;

		result1 = digraph.addEdge(begin, end, edgeWeight);
		result2 = digraph.addEdge(end, begin, edgeWeight);

        boolean result = false;
        if(result1 && result2)
            result = true;

		return result;
	}


	public boolean addEdge(T begin, T end) {
		return addEdge(begin,end, 0);
	}


	public boolean hasEdge(T begin, T end) {
		return digraph.hasEdge(begin, end);
	}


	public boolean isEmpty() {
		return digraph.isEmpty();
	}


	public int getNumberOfVertices() {
		return digraph.getNumberOfVertices();
	}


	public int getNumberOfEdges() {
		return digraph.getNumberOfEdges() / 2;
	}


	public void clear() {
        digraph.clear();
	}

	public Queue<T> getBreadthFirstTraversal(T origin) {
		return digraph.getBreadthFirstTraversal(origin); //Assumes origin is present in graph
	}

	public Queue<T> getDepthFirstTraversal(T origin) {
		return digraph.getBreadthFirstTraversal(origin); //Assumes origin is present in graph
	}

    public void display(){
        digraph.display();
    }

	public boolean isConnected(T origin) {
        Queue check = getBreadthFirstTraversal(origin);
        int counter = 0;

        while(check.peek() != null)
        {
            check.remove();
            counter++;
        }

		if(counter == getNumberOfVertices())
            return true;
        else
            return false;
	}

}
