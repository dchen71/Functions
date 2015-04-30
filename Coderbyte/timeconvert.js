//Converts num into the hours and minutes

function TimeConvert(num) { 

  // code goes here  
  var minutes = num%60;
  var hours = Math.floor(num/60);
  return hours.toString() + ":" + minutes.toString(); 
         
}
   
// keep this function call here 
// to see how to enter arguments in JavaScript scroll down
TimeConvert(readline());           
