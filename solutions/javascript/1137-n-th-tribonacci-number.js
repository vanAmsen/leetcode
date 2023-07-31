var tribonacci = function(n) {
    if (n == 0) return 0;
    if (n <= 2) return 1;
    let a = 0, b = 1, c = 1;
    for (let i = 0; i < n - 2; i++) {
        let temp = a + b + c;
        a = b;
        b = c;
        c = temp;
    }
    return c;
};
