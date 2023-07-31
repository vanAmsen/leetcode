public class Solution {
    public int[] CountBits(int n) {
        int[] res = new int[n + 1];
        for(int i = 1; i <= n; i++)
            res[i] = res[i >> 1] + (i & 1);
        return res;
    }
}
