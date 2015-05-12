//Determines the number of breaks needed to break down a nxm chocolate into into 1x1

public class Chocolate{
  public static int breakChocolate(int n, int m) {
    int answer = 0;
    
    if(n < 1 || m < 1)
      return 0;
    
    for(int i = n; i > 0; i--)
    {
      for(int j = m; j > 0; j--)
        answer += 1;
    }
    return(answer - 1);
  }
  
}


/*
import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class MyTester {
  
  @Test
  public void myTests() {
    assertEquals(Chocolate.breakChocolate(5, 5) , 24);
    assertEquals(Chocolate.breakChocolate(1, 1) , 0);
  }
}
 */