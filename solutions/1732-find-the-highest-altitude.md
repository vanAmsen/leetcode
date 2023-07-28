# 🎯 Finding the Longest Subarray of 1's After Deleting One Element

# Intuition
My first thought to solve this problem is to use an incremental approach. Given that we start at altitude 0, we can keep adding the 'gain' at each step to get the new altitude and track the maximum altitude reached at any point. This approach makes sense as the altitude at a given point is simply the sum of all the gains till that point.

# Approach
We start by initializing two variables, 'max_altitude' and 'current_altitude', both to 0. Then, we loop through the 'gain' list, adding each value to 'current_altitude'. After each addition, we compare 'current_altitude' with 'max_altitude'. If 'current_altitude' is greater, we update 'max_altitude' to the new value. The logic behind this is simple - we are climbing up (or down) a mountain, and we keep track of the highest point we've reached so far. Once we've gone through the entire list, we return 'max_altitude' as the highest altitude reached.

# Complexity
- Time complexity:
The time complexity of this solution is O(n), where n is the length of the 'gain' list. This is because we are traversing the 'gain' list once.

- Space complexity:
The space complexity of the solution is O(1). This is because we are using a constant amount of space to store the current and maximum altitudes, regardless of the input size.

# Code
```python []
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_altitude = 0 
        current_altitude = 0    
        for g in gain: 
            current_altitude += g 
            if current_altitude > max_altitude: 
                max_altitude = current_altitude 
        return max_altitude 
```
```javascript []
var largestAltitude = function(gain) {
    let maxAltitude = 0;
    let currentAltitude = 0;
    
    for(let g of gain) {
        currentAltitude += g;
        if(currentAltitude > maxAltitude)
            maxAltitude = currentAltitude;
    }
    return maxAltitude;
};
```
```rust []
impl Solution {
    pub fn largest_altitude(gain: Vec<i32>) -> i32 {
        let mut max_altitude = 0;
        let mut current_altitude = 0;

        for &g in gain.iter() {
            current_altitude += g;
            if current_altitude > max_altitude {
                max_altitude = current_altitude;
            }
        }
        max_altitude
    }
}
```
```Go []
func largestAltitude(gain []int) int {
    maxAltitude := 0
    currentAltitude := 0
    
    for _, g := range gain {
        currentAltitude += g
        if currentAltitude > maxAltitude {
            maxAltitude = currentAltitude
        }
    }
    return maxAltitude
}

```
```C# []
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
```
