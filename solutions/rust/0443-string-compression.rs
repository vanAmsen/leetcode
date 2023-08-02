impl Solution {
    pub fn compress(chars: &mut Vec<char>) -> i32 {
        let mut write_index = 0;
        let mut read_index = 0;

        while read_index < chars.len() {
            let char = chars[read_index];
            let mut count = 0;

            while read_index < chars.len() && chars[read_index] == char {
                read_index += 1;
                count += 1;
            }

            chars[write_index] = char;
            write_index += 1;

            if count > 1 {
                for digit in count.to_string().chars() {
                    chars[write_index] = digit;
                    write_index += 1;
                }
            }
        }

        write_index as i32
    }
}
