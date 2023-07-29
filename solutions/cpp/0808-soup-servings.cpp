class Solution {
public:
    double soupServings(int N) {
        if (N > 4451) {
            return 1.0;
        }
        N = (N + 24) / 25;
        std::unordered_map<int, double> memo;

        return dp(N, N, memo);
    }

private:
    double dp(int a, int b, std::unordered_map<int, double>& memo) {
        if (a <= 0 && b <= 0) {
            return 0.5;
        }
        if (a <= 0) {
            return 1.0;
        }
        if (b <= 0) {
            return 0.0;
        }
        int key = a * 5000 + b;
        if (memo.count(key)) {
            return memo[key];
        }
        memo[key] = 0.25 * (dp(a-4, b, memo) + dp(a-3, b-1, memo) + dp(a-2, b-2, memo) + dp(a-1, b-3, memo));
        return memo[key];
    }
};
