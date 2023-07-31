public class Solution {
    public int MinCostClimbingStairs(int[] cost) {
        int f1 = 0, f2 = 0;
        for (int i = cost.Length - 1; i >= 0; --i) {
            int f0 = cost[i] + Math.Min(f1, f2);
            f2 = f1;
            f1 = f0;
        }
        return Math.Min(f1, f2);
    }
}
