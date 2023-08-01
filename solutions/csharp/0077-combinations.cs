public class Solution {
    public IList<IList<int>> Combine(int n, int k) {
        var result = new List<IList<int>>();
        GenerateCombinations(1, n, k, new List<int>(), result);
        return result;
    }
    
    private void GenerateCombinations(int start, int n, int k, List<int> combination, IList<IList<int>> result) {
        if (k == 0) {
            result.Add(new List<int>(combination));
            return;
        }
        for (var i = start; i <= n; ++i) {
            combination.Add(i);
            GenerateCombinations(i + 1, n, k - 1, combination, result);
            combination.RemoveAt(combination.Count - 1);
        }
    }
}
