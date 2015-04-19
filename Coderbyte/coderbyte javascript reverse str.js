/*
For this challenge you will be reversing a string.
*/

function FirstReverse(str) { 
var reverse = "";
var sLength = str.length;
  for(i=0;i< str.length; i++)
  {
  	reverse = reverse + str.charAt(sLength - 1 - i);
  }
  // code goes here  
  return reverse; 
         
}
   
// keep this function call here 
// to see how to enter arguments in JavaScript scroll down
FirstReverse(readline());                            















                            
                            
                            
  