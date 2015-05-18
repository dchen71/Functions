//Takes str as parameter and replace each letter with one character in front ex. a=>b b=>c and capitalize all vowels

function LetterChanges(str) { 
  var letters = new Array();
  
  //Setup dictionary like array
  var letters = {'a' : 'b','b' : 'c','c' : 'd','d' : 'E','e':'f', 'f' : 'g','g' : 'h','h' : 'I','i' : 'j','j' : 'k',
  				'k' : 'l','l' : 'm','m' : 'n','n' : 'O','o' : 'p','p' : 'q','q' : 'r','r' : 's','s' : 't','t' : 'U',
  				'u' : 'v','v' : 'w','w' : 'x','x' : 'y','y' : 'z','z' : 'A'};

  var answer = "";
  var compare = str.toLowerCase(); //standardize all chars to be lowercase
  
  //Has weird issue with certain characters in array returning as true
  //ex letters['a'] = true and e
  //go look up assocative arrays and figure out why certain variables returns true
  //backwards but could try converting chars to number code to then use that to find up a version using arrays

  for(letter in compare){
    if(letters[letter] =! null)
    	answer = answer.concat(letters[letter]);
    else
    	answer = answer.concat(letter);
  }
 
 
  
  // code goes here  
  return answer; 
         
}
   
// keep this function call here 
// to see how to enter arguments in JavaScript scroll down
LetterChanges(readline());                            















                            
                            
                            
  