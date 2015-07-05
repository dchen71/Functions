/*
Algorithm: Magazine -
Sets up new magazines and can return magazines as string
*/


public class Magazine
{
	String title;

//Sets up new magazine with its title
	public Magazine(String newTitle)
	{
		title = newTitle;
	}

//Returns magazine as string
	public String toString ()
	{
		return title;
	}
}
