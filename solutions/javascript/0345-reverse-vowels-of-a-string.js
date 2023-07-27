/**
 * @param {string} s
 * @return {string}
 */
var reverseVowels = function(s) {
    let start = 0, end = s.length - 1;
    const vowels = new Set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']);
    let arr = s.split('');

    while (start < end) {
        if (vowels.has(arr[start]) && vowels.has(arr[end])) {
            [arr[start++], arr[end--]] = [arr[end], arr[start]];
        } else if (vowels.has(arr[start])) {
            end--;
        } else {
            start++;
        }
    }
    return arr.join('');
};
