class Solution {
    public int candy(int[] ratings) {
        if(ratings.length == 0){
            return 0;
        }

        int ret = 1, up = 0, down = 0, peak = 0;

        for(int i = 0; i < ratings.length - 1; i++){
            int prev = ratings[i], curr = ratings[i+1];

            if(prev < curr){
                up++;
                down = 0;
                peak = up;
                ret += 1 + up;
            } else if (prev == curr){
                up = 0;
                down = 0;
                peak = 0;
                ret += 1;
            } else {
                up = 0;
                down++;
                ret += 1 + down;
                if (peak >= down){
                    ret--;
                }
            }
        }

        return ret;
    }
}