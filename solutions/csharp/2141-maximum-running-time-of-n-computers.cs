public class Solution {
    public long MaxRunTime(int n, int[] batteries) {
        Array.Sort(batteries);
        long left = 1, right = (long)batteries.Sum(b => (long)b) / n;
        while (left < right) {
            long target = right - (right - left) / 2;
            long total = batteries.Sum(battery => Math.Min((long)battery, target));
            if (total >= target * n) {
                left = target;
            } else {
                right = target - 1;
            }
        }
        return left;
    }
}
