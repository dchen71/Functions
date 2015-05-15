//Finds the largest word in a string ignoring punctuation and non empty parameter

//Currently does not deal with nonspecial characters

function LongestWord(sen) { 
    var word = null;
  	var longest = 0;
  	var arrayWord = sen.split(" ");

  	for(i = 0; i < arrayWord.length; i++){
      var cur = arrayWord[i];
      var curLen = cur.length;
      if(longest < curLen){
        longest = curLen;
        word = arrayWord[i];
      }
    }
        
  	// code goes here  
  	return word; 
         
}
   
// keep this function call here 
// to see how to enter arguments in JavaScript scroll down
LongestWord(readline());                            
