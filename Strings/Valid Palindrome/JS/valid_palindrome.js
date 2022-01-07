/**
 * @param {string} s
 * @return {boolean}
 */
 var isPalindrome = function(s) {
    s = s.replace(/\W+|_+/g, "").toLowerCase();
    
    for (let i = 0; i < s.length; i++){
        if (s[i] != s[s.length - 1 - i]){
            return false;
        }
    }
    return true;
};

let test_s = "ab_a"
console.log(`string ${test_s} palindrome? - ${isPalindrome(test_s)}`);