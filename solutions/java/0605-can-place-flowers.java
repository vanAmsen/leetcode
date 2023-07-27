class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        int[] bed = new int[flowerbed.length + 2];
        System.arraycopy(flowerbed, 0, bed, 1, flowerbed.length);
        for (int i = 1; i < bed.length - 1; ++i) {
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
