//Takes the input number and returns the factorial of that number
//Factorial = num!
function FirstFactorial(num) { 
  var fact = num;
 
  for(i=num;i>1;i--)
  {
    fact = fact * (i - 1);
  }
  
  return fact; 
         
}
   
FirstFactorial(readline());                            


