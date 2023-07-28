class Solution {
    public int largestAltitude(int[] gain) {
        int max_altitude = 0;
        int current_altitude = 0;
        for(int g : gain){
            current_altitude += g;
            max_altitude = Math.max(current_altitude, max_altitude);
        }
        return max_altitude;
    }
}
