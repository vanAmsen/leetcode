impl Solution {
    pub fn word_break(s: String, word_dict: Vec<String>) -> bool {
        let n = s.len();
        let mut dp = vec![false; n + 1];
        dp[0] = true;
        let max_len = word_dict.iter().map(|word| word.len()).max().unwrap_or(0);

        let word_dict: std::collections::HashSet<String> = word_dict.into_iter().collect();

        for i in 1..=n {
            for j in (std::cmp::max(i as isize - max_len as isize - 1, 0) as usize..i).rev() {
                if dp[j] && word_dict.contains(&s[j..i].to_string()) {
                    dp[i] = true;
                    break;
                }
            }
        }

        dp[n]
    }
}
