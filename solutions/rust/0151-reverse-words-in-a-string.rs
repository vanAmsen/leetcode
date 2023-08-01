impl Solution {
    pub fn reverse_words(s: String) -> String {
        let words: Vec<&str> = s.split_whitespace().collect();
        let reversed_words: Vec<&str> = words.into_iter().rev().collect();
        reversed_words.join(" ")
    }
}
