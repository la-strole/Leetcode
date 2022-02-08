/**
 * @param {number[]} prices
 * @return {number}
 */
 var maxProfit = function(prices) {
    
    let localMinimum = 0;
    let localMaximum = 1;
    let maxMargin = 0;

    while (localMaximum < prices.length) {
        // if function is decreasing
        if (prices[localMaximum] < prices[localMinimum]) {
            localMinimum = localMaximum;
        }
        // if function is increasing we can get margin
        else { 
            maxMargin = Math.max((prices[localMaximum] - prices[localMinimum]), maxMargin);
        }
        // moove local maximum pointer
        localMaximum++;
    }
    return maxMargin;
};