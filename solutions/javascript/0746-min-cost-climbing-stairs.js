/**
 * @param {number[]} cost
 * @return {number}
 */
var minCostClimbingStairs = function(cost) {
    let f1 = 0, f2 = 0;
    for (let i = cost.length - 1; i >= 0; --i) {
        let f0 = cost[i] + Math.min(f1, f2);
        f2 = f1;
        f1 = f0;
    }
    return Math.min(f1, f2);
};
