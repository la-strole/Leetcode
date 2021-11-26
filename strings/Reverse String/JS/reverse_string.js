/**
 * @param {character[]} s
 * @return {void} Do not return anything, modify s in-place instead.
 */
var reverseString = function(s) {
  for (let i = 0, j = s.length - 1; i < j; i++, j--){
    let tmp = s[i];
    s[i] = s[j];
    s[j] = tmp;
  }
};

let s = ["h", "e", "l", "l", "o"];
reverseString(s);
console.log(s);