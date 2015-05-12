//Disembowels all vowels in a string

function disemvowel(str) {
  answer = str.replace(/a/gi,"");
  answer = answer.replace(/e/gi,"");
  answer = answer.replace(/i/gi,"");
  answer = answer.replace(/o/gi,"");
  answer = answer.replace(/u/gi,"");
  return answer;
}