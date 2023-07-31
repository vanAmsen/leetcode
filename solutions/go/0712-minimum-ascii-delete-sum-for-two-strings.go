func minimumDeleteSum(s1 string, s2 string) int {
    prev_row := make([]int, len(s2) + 1)
    for j := 1; j <= len(s2); j++ {
        prev_row[j] = prev_row[j - 1] + int(s2[j - 1])
    }

    for i := 1; i <= len(s1); i++ {
        curr_row := []int{prev_row[0] + int(s1[i - 1])}
        for j := 1; j <= len(s2); j++ {
            if s1[i - 1] == s2[j - 1] {
                curr_row = append(curr_row, prev_row[j - 1])
            } else {
                curr_row = append(curr_row, min(prev_row[j] + int(s1[i - 1]), curr_row[j - 1] + int(s2[j - 1])))
            }
        }
        prev_row = curr_row
    }

    return prev_row[len(prev_row) - 1]
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}
