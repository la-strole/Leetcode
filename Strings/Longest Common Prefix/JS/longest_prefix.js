/**
 * @param {string[]} strs
 * @return {string}
 */
 var longestCommonPrefix = function(strs) {

    let result = '';
    for (let i = 0; i < strs[0].length; i++){
        let letter = strs[0][i];
        for (s of strs){
            try {
                if (s[i] != letter){
                    return result;
                }
            }
            catch(RangeError){
                return result;
            }
        }
        result = result + letter;
    }
    return result;
};

var longestCommonPrefix_v2 = function(strs) {
    let charIndex = 0;
    let prefix = [];
    
    while (true) {
      let expectedChar = strs[0][charIndex];
      
      for (const word of strs) {
        if (charIndex >= word.length) return prefix.join('');
        if (word[charIndex] !== expectedChar) return prefix.join('');
      }
      
      prefix.push(expectedChar);
      charIndex++;
    }
    
    return prefix.join('');
  };