/**
 * @param {string} a
 * @param {string} b
 * @param {string} c
 * @return {string}
 */
var minimumString = function(a, b, c) {
    function merge(s1, s2) {
        if (s1.includes(s2)) {
            return s1;
        }
        for (let i = 0; i < s1.length; i++) {
            if (s2.startsWith(s1.substring(i))) {
                return s1.substring(0, i) + s2;
            }
        }
        return s1 + s2;
    }

    let res = '';
    let l = Infinity;
    for (let s of [
        merge(merge(a, b), c),
        merge(merge(b, a), c),
        merge(merge(c, b), a),
        merge(merge(b, c), a),
        merge(merge(a, c), b),
        merge(merge(c, a), b)
    ]) {
        if (s.length < l) {
            res = s;
            l = s.length;
        } else if (s.length === l) {
            res = res < s ? res : s;
        }
    }

    return res;
};
