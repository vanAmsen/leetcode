public class Solution {
    public int LargestAltitude(int[] gain) {
        int maxAltitude = 0; 
        int currentAltitude = 0; 

        foreach(int g in gain){ 
            currentAltitude += g; 
            if(currentAltitude > maxAltitude) 
                maxAltitude = currentAltitude; 
        } 
        return maxAltitude; 
                                                                                            
    }
}
