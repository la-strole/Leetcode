/**
 * Definition for isBadVersion()
 * 
 * @param {integer} version number
 * @return {boolean} whether the version is bad
 * isBadVersion = function(version) {
 *     ...
 * };
 */

/**
 * @param {function} isBadVersion()
 * @return {function}
 */
 var solution = function(isBadVersion) {
    /**
     * @param {integer} n Total versions
     * @return {integer} The first bad version
     */
    return function(n) {
        
        let low = 1;
        let hi = n;

        while (low < hi) {

            let mid = low + Math.floor((hi - low) / 2);

            if (isBadVersion(mid) === true) {
                hi = mid;
            }
            else {
                low = mid + 1;
            }

        }

        return low;
    };
};