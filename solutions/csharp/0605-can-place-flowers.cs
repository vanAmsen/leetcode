public class Solution {
    public bool CanPlaceFlowers(int[] flowerbed, int n) {
        int[] bed = new int[flowerbed.Length + 2];
        Array.Copy(flowerbed, 0, bed, 1, flowerbed.Length);
        for (int i = 1; i < bed.Length - 1; ++i) {
            if (bed[i - 1] == 0 && bed[i] == 0 && bed[i + 1] == 0) {
                bed[i] = 1;
                --n;
            }
            if (n == 0)
                return true;
        }
        return n <= 0;
    }
}
