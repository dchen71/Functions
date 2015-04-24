//Checks and returns boolean if a number is prime or not

function PrimeTime(num) { 

  // code goes here  
  if (num ==2)
    return true;
   else if (num == 3)
     return true;
  else if (num == 5)
    return true;
  else if (num == 7)
    return true;
  
  if(num %2 == 0)
    return false;
  else if (num % 3 == 0)
    return false;
  else if (num%5 == 0)
    return false;
  else if (num%7 ==0)
    return false;
  else
    return true;
}
   
// keep this function call here 
// to see how to enter arguments in JavaScript scroll down
PrimeTime(readline());           
