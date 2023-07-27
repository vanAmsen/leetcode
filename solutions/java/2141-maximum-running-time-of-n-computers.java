public class Solution {
    public long maxRunTime(int n, int[] batteries) {
        Arrays.sort(batteries);
        long left = 1, right = (long)Arrays.stream(batteries).asLongStream().sum() / n;
        while (left < right) {
            long target = right - (right - left) / 2;
            long total = Arrays.stream(batteries).asLongStream().map(battery -> Math.min(battery, target)).sum();
            if (total >= target * n) {
                left = target;
            } else {
                right = target - 1;
            }
        }
        return left;
    }
}
