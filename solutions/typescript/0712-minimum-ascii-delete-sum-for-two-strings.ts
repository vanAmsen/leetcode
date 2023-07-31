function minimumDeleteSum(s1: string, s2: string): number {
    let prev_row: number[] = new Array(s2.length + 1).fill(0);
    for (let j = 1; j <= s2.length; j++) {
        prev_row[j] = prev_row[j - 1] + s2.charCodeAt(j - 1);
    }

    for (let i = 1; i <= s1.length; i++) {
        let curr_row: number[] = [prev_row[0] + s1.charCodeAt(i - 1)];
        for (let j = 1; j <= s2.length; j++) {
            if (s1[i - 1] === s2[j - 1]) {
                curr_row.push(prev_row[j - 1]);
            } else {
                curr_row.push(Math.min(prev_row[j] + s1.charCodeAt(i - 1), curr_row[j - 1] + s2.charCodeAt(j - 1)));
            }
        }
        prev_row = curr_row;
    }

    return prev_row[prev_row.length - 1];
}
