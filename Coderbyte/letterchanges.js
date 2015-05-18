//Takes str as parameter and replace each letter with one character in front ex. a=>b b=>c and capitalize all vowels

function LetterChanges(str) { 
  var letters = new Array();
  
  //Setup dictionary like array
  letters['a'] = 'b';
  letters['b'] = 'c';
  letters['c'] = 'd';
  letters['d'] = 'E';
  letters['e'] = 'f';
  letters['f'] = 'g';
  letters['g'] = 'h';
  letters['h'] = 'I';
  letters['i'] = 'j';
  letters['j'] = 'k';
  letters['k'] = 'l';
  letters['l'] = 'm';
  letters['m'] = 'n';
  letters['n'] = 'O';
  letters['o'] = 'p';
  letters['p'] = 'q';
  letters['q'] = 'r';
  letters['r'] = 's';
  letters['s'] = 't';
  letters['t'] = 'U';
  letters['u'] = 'v';
  letters['v'] = 'w';
  letters['w'] = 'x';
  letters['x'] = 'y';
  letters['y'] = 'z';
  letters['z'] = 'A';

  var answer = ""
  var compare = str.toLowerCase();
  
  //Has weird issue with certain characters in array returning as true
  //ex letters['a'] = true and e
  for(i = 0; i <= str.length; i++){
    if(letters[compare.charAt(i)] =! null)
    	answer = answer.concat(letters[compare.charAt(i)]);
    else
    	answer = answer.concat(compare.charAt(i));
  }
 
 
  
  // code goes here  
  return answer; 
         
}
   
// keep this function call here 
// to see how to enter arguments in JavaScript scroll down
LetterChanges(readline());                            















                            
                            
                            
  