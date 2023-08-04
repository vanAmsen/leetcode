func wordBreak(s string, wordDict []string) bool {
    n := len(s)
    dp := make([]bool, n+1)
    dp[0] = true
    max_len := 0
    for _, word := range wordDict {
        if len(word) > max_len {
            max_len = len(word)
        }
    }

    for i := 1; i <= n; i++ {
        for j := i - 1; j >= max(i - max_len - 1, 0); j-- {
            if dp[j] && contains(wordDict, s[j:i]) {
                dp[i] = true
                break
            }
        }
    }

    return dp[n]
}

func contains(words []string, target string) bool {
    for _, word := range words {
        if word == target {
            return true
        }
    }
    return false
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
