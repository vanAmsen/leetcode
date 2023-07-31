class Solution {
    func minimumDeleteSum(_ s1: String, _ s2: String) -> Int {
        var prevRow = [Int](repeating: 0, count: s2.count + 1)
        let s1 = Array(s1.unicodeScalars)
        let s2 = Array(s2.unicodeScalars)
        
        for j in 1...s2.count {
            prevRow[j] = prevRow[j - 1] + Int(s2[j - 1].value)
        }

        for i in 1...s1.count {
            var currRow = [prevRow[0] + Int(s1[i - 1].value)]
            for j in 1...s2.count {
                if s1[i - 1] == s2[j - 1] {
                    currRow.append(prevRow[j - 1])
                } else {
                    currRow.append(min(prevRow[j] + Int(s1[i - 1].value), currRow[j - 1] + Int(s2[j - 1].value)))
                }
            }
            prevRow = currRow
        }
        return prevRow.last!
    }
}
