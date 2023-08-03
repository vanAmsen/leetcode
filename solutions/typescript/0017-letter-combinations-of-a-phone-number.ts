function letterCombinations(digits: string): string[] {
    if (digits.length === 0) return [];

    const phoneMap: string[] = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"];
    const output: string[] = [];

    function backtrack(combination: string, nextDigits: string) {
        if (nextDigits.length === 0) {
            output.push(combination);
        } else {
            const letters: string = phoneMap[parseInt(nextDigits[0]) - 2];
            for (const letter of letters) {
                backtrack(combination + letter, nextDigits.slice(1));
            }
        }
    }

    backtrack("", digits);
    return output;
}
