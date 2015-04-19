/*
Using the JavaScript language, have the function FirstFactorial(num) take the num parameter being passed and return the factorial of it (ie. if num = 4, return (4 * 3 * 2 * 1)). For the test cases, the range will be between 1 and 18.

Use the Parameter Testing feature in the box below to test your code with different arguments. 
*/

function FirstFactorial(num) { 
  var fact = num;
 
  for(i=num;i>1;i--)
  {
    fact = fact * (i - 1);
  }
  
  return fact; 
         
}
   
FirstFactorial(readline());                            


