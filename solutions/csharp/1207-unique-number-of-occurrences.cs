public class Solution {
    public bool UniqueOccurrences(int[] arr) {
        Dictionary<int, int> count = new Dictionary<int, int>();
        foreach (int num in arr) {
            if (count.ContainsKey(num)) {
                count[num]++;
            } else {
                count[num] = 1;
            }
        }
        HashSet<int> uniqueCount = new HashSet<int>(count.Values);
        return uniqueCount.Count == count.Count;
    }
}
