class Solution {
		func strangePrinter(_ s: String) -> Int {
			let s = Array(s)
			let n = s.count
			var dp = Array(repeating: Array(repeating: 0, count: n), count: n)

			for i in stride(from: n-1, through: 0, by: -1) {
					dp[i][i] = 1
					for j in i+1..<n {
							dp[i][j] = dp[i][j-1] + 1
							for k in i..<j {
									if s[k] == s[j] {
											dp[i][j] = min(dp[i][j], dp[i][k] + (k+1<=j-1 ? dp[k+1][j-1] : 0))
									}
							}
					}
			}

			return dp[0][n-1]
	}
}
