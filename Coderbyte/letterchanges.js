//Takes str as parameter and replace each letter with one character in front ex. a=>b b=>c and capitalize all vowels

function LetterChanges(str) { 
  var letters = new Array();
  
  //Setup dictionary like array
  var code = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f' :5, 'g':6, 'h': 7, 'i':8,'j':9,
  				'k':10,'l':11,'m':12, 'n':13, 'o':14,'p':15, 'q':16, 'r':17, 's':18,'t':19,
  				'u':20,'v':21,'w':22,'x':23,'y':24,'z':25};

  var letters = 'bcdEfghIjklmnOpqrstUvwxyzA';

  var answer = "";
  var compare = str.toLowerCase(); //standardize all chars to be lowercase
  
  //Has weird issue with certain characters in array returning as true
  //ex letters['a'] = true and e
  //go look up assocative arrays and figure out why certain variables returns true
  //backwards but could try converting chars to number code to then use that to find up a version using arrays

  for(i=0;i< str.length; i++){
    if(!code[compare[i]] == false)
    	answer = answer.concat(letters[code[compare[i]]]);
    else
    	answer = answer.concat(compare[i]);
  }
 
 
  
  // code goes here  
  return answer; 
         
}
   
// keep this function call here 
// to see how to enter arguments in JavaScript scroll down
LetterChanges(readline());                            
