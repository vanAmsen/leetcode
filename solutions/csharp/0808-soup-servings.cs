public class Solution {
    Dictionary<Tuple<int, int>, double> memo = new Dictionary<Tuple<int, int>, double>();

    public double SoupServings(int N) {
        if (N > 4451) {
            return 1.0;
        }
        N = (N + 24) / 25;

        return dp(N, N);
    }

    private double dp(int a, int b) {
        if (a <= 0 && b <= 0) {
            return 0.5;
        }
        if (a <= 0) {
            return 1.0;
        }
        if (b <= 0) {
            return 0.0;
        }
        var key = Tuple.Create(a, b);
        if (memo.ContainsKey(key)) {
            return memo[key];
        }
        memo[key] = 0.25 * (dp(a-4, b) + dp(a-3, b-1) + dp(a-2, b-2) + dp(a-1, b-3));
        return memo[key];
    }
}
