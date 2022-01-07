/**
 * @param {string} s
 * @return {number}
 */
 var firstUniqChar = function(s) {
    const hash_table = new Map();

    /* create hash table key - alpha letter, \
    value - list [is_unique, first_index]*/
    for (let i = 0; i < s.length; i++){
        let letter = s.charAt(i);
        if (hash_table.has(letter)){
            hash_table.get(letter)[0] = false;
        }
        else{
            hash_table.set(letter, [true, i]);
        }
    }
    /* walk trough hash table to look for true unique elements in ordered dict map*/
    for (let value of hash_table.values()){
        if (value[0] === true){
            return value[1];
        }
    }
    return -1;
};

var firstUniqChar_v2 = function(s) {
    
    let uniqueChars = new Map();
    
    for(let i = 0; i < s.length; i++) {
        if(uniqueChars.has(s[i])) {
            uniqueChars.get(s[i]).push(i);
        } else {
            uniqueChars.set(s[i], [i]);
        }
    }
    
    
    for(const [key, value] of uniqueChars) {
        
        if(value.length == 1) {
          return value[0];
        } 
    }
    
    return -1;
    
};

let test_s = "aabb";
console.log(`first unique char in "${test_s}" is ${firstUniqChar(test_s)}`);