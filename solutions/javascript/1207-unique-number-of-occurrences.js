/**
 * @param {number[]} arr
 * @return {boolean}
 */
var uniqueOccurrences = function(arr) {
    let count = {};
    for (let num of arr) {
        if (num in count) {
            count[num]++;
        } else {
            count[num] = 1;
        }
    }
    let uniqueCount = new Set(Object.values(count));
    return uniqueCount.size === Object.keys(count).length;    
};
