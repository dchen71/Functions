//Takes str as parameter and replace each letter with one character in front ex. a=>b b=>c and capitalize all vowels

function LetterChanges(str) { 
  var letters = new Array();
  
  //Setup dictionary like array
  var code = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f' :6, 'g':7, 'h': 8, 'i':9,'j':10,
  				'k':11,'l':12,'m':13, 'n':14, 'o':15,'p':16, 'q':17, 'r':18, 's':19,'t':20,
  				'u':21,'v':22,'w':23,'x':24,'y':25,'z':26};

  var letters = ' bcdEfghIjklmnOpqrstUvwxyzA'; //Pool of characters moved up 1

  var answer = "";
  var compare = str.toLowerCase(); //standardize all chars to be lowercase
  
  for(i=0;i< str.length; i++){
    if(!code[compare.charAt(i)] == false)
    	answer = answer.concat(letters.charAt(code[compare.charAt(i)]));
    else
    	answer = answer.concat(compare.charAt(i));
  }
  
  // code goes here  ;
  return answer; 
         
}
   
// keep this function call here 
// to see how to enter arguments in JavaScript scroll down
LetterChanges(readline());                            
