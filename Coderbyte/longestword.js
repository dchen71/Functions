//Finds the largest word in a string ignoring punctuation and non empty parameter

function LongestWord(sen) { 
    var word = null;
  	var longest = 0;
  	var removeSpec = sen.replace(/[^\w]/g, " "); //regex out anything not starting with a-z A-Z, \w = a-zA-Z,/g = global
  	var arrayWord = removeSpec.split(" "); //splits string sans space into array

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

