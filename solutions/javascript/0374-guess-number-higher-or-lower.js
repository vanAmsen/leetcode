/**
 * @param {number} n
 * @return {number}
 */
var guessNumber = function(n) {
    let left = 1, right = n;
    while (left <= right) {
        let mid = Math.floor(left + (right - left) / 2);
        let res = guess(mid);
        if (res === 0) {
            return mid;
        } else if (res < 0) {
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
    return -1;
};
