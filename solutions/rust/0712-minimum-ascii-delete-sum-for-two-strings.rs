impl Solution {
    pub fn minimum_delete_sum(s1: String, s2: String) -> i32 {
        let mut prev_row = vec![0; s2.len() + 1];
        let s1 = s1.chars().collect::<Vec<_>>();
        let s2 = s2.chars().collect::<Vec<_>>();

        for j in 1..=s2.len() {
            prev_row[j] = prev_row[j - 1] + s2[j - 1] as i32;
        }

        for i in 1..=s1.len() {
            let mut curr_row = vec![prev_row[0] + s1[i - 1] as i32];
            for j in 1..=s2.len() {
                if s1[i - 1] == s2[j - 1] {
                    curr_row.push(prev_row[j - 1]);
                } else {
                    curr_row.push(std::cmp::min(prev_row[j] + s1[i - 1] as i32, curr_row[j - 1] + s2[j - 1] as i32));
                }
            }
            prev_row = curr_row;
        }

        *prev_row.last().unwrap()
    }
}
