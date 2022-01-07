/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
 var isAnagram = function(s, t) {
    
    if (s.length != t.length){
        return false;
    }

    const hash_table = new Map();
    /* create hash table */
    for (let i = 0; i < s.length; i++){
        if (hash_table.has(s[i])){
            hash_table.set(s[i], hash_table.get(s[i]) + 1);
        }
        else{
            hash_table.set(s[i], 1);
        }
        
        if (hash_table.has(t[i])){
            hash_table.set(t[i], hash_table.get(t[i]) - 1);
        }
        else{
            hash_table.set(t[i], -1);
        }
       
    }
    console.log(hash_table);
    for (let i of hash_table.values()){
        console.log(`i in hash values is ${i}`);
        if (i !== 0){
            return false;
        }
    }
    return true;
};

let test_s = "anagram";
let test_t = "nagaram";
console.log(`'${test_s}' and '${test_t}' are anarams? - ${isAnagram(test_s, test_t)}`);