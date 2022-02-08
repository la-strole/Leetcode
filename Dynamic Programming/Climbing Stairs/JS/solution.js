/**
 * @param {number} n
 * @return {number}
 */
 var climbStairs = function(n) {
    
    if (n <= 3) {
        return n;
    }

    let n1 = 1;
    let n2 = 2;
    let helper = 0;

    for (let i = 3; i < n + 1; i++) {
        helper = n1;
        n1 = n2;
        n2 = n1 + helper;
    }

    return n2;

};