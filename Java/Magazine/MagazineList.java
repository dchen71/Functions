/*
Algorithm: MagazineList -
Setups up a list
Can do tail insertion of magazines
Can do head insertion of magazines
Can delete all magazines
Can delete a magazine if present
Makes list of magazine as a String
Uses nodes as a representation of the list of magazines
*/


public class MagazineList
{
	private MagazineNode list;

//Constructor
	public MagazineList()
	{
		list = null;
	}

//Does tail insertion of magazines
	public void add(Magazine mag)
	{
		MagazineNode node = new MagazineNode(mag);
		MagazineNode current;

		if(list == null)
			list = node;
		else
		{
			current = list;
			while(current.next != null)
				current = current.next;
			current.next = node;
		}
	}

//Head inserts new magazine entry
	public void insert(Magazine mag)
	{
	  MagazineNode node = new MagazineNode (mag);

    //First node will point to the current root
	  node.next = list;

    //Root becomes the new first node
	  list = node;
	}

//Method sets list to null to delete all the magazines
	public void deleteAll()
	{
		if(list != null)
            list = null;
	}

//Deletes a magazine of choice if present
	public void delete (Magazine mag)
	{
	    MagazineNode current = this.list;
	    MagazineNode title = new MagazineNode(mag);
	    MagazineNode old;
        MagazineNode third;

	    String checkM = title.magazine.toString();
	    String presentM = current.magazine.toString();

	    //Checks 1st element and can replace with 3rd if it sees it following
	    if (presentM.equalsIgnoreCase(checkM))
	    {
	        third = current.next;
            String thirdM = third.magazine.toString();

	        if(presentM.equalsIgnoreCase(thirdM))
                this.list = third.next;
            else
                this.list = current.next;
	    }
	    old = current;

	    //Checks other elements
	    while ((current = current.next) != null)
	    {
		   presentM = current.magazine.toString();

	        //if is the current element
	        if (presentM.equalsIgnoreCase(checkM))
	        {
	                old.next = current.next;
            }
	            old = current;
        }
    }

//Returns list of magazines as a string
	public String toString()
	{
		String result = "";

		MagazineNode current = list;

		while (current != null)
		{
			result += current.magazine + "\n";
			current = current.next;
		}
		return result;
	}

//Represents magazines with nodes
	private class MagazineNode
	{
		public Magazine magazine;
		public MagazineNode next;

        //Sets up node
		public MagazineNode(Magazine mag)
		{
			magazine = mag;
			next = null;
		}
	}
}
