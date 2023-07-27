# Intuition
When I first read this problem, I realized that it's not just about using each battery to its full capacity before moving on to the next. The goal here is to maximize the running time of all computers, and a simple linear approach would not achieve that. The challenge here lies in striking a balance between using batteries that have the most power and ensuring that no energy is wasted.

# Approach
The approach I took for this problem is to find a balance between using batteries that have the most power and ensuring that no energy is wasted. I employed a binary search strategy to locate the maximum possible running time. 

Initially, I set 1 as the left boundary and the total power of all batteries divided by 'n' as the right boundary. In the binary search, I set a target running time and checked if we could reach this target with the available batteries. If we could, I updated the left boundary to the target. If we couldn't, I updated the right boundary to one less than the target. I continued this process until the left and right boundaries met, at which point we've found the maximum possible running time.

# Complexity
- Time complexity: The time complexity for this problem is \(O(m \cdot \log k)\), where \(m\) is the length of the input array batteries and \(k\) is the maximum power of one battery.

- Space complexity: The space complexity for this problem is \(O(1)\). During the binary search, we only need to record the boundaries of the searching space and the power extra, and the accumulative sum of extra, which only takes constant space.

# Code
```Python
class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        left, right = 1, sum(batteries) // n 
        while left < right: 
            target = right - (right - left) // 2 
            if sum(min(battery, target) for battery in batteries) >= target * n: 
                left = target 
            else: 
                right = target - 1 
        return left 
```                                                                                                      
# Code Solutions
- [Python](python/2141-maximum-running-time-of-n-computers.py)
- [C++](cpp/2141-maximum-running-time-of-n-computers.cpp)
- [Java](java/2141-maximum-running-time-of-n-computers.java)
- [C#](csharp/2141-maximum-running-time-of-n-computers.cs)
- [JavaScript](javascript/2141-maximum-running-time-of-n-computers.js)

# Video Solutions
- [Python](https://youtu.be/xnkXF1Yed94)

Please replace the URL with the actual URL of the video where you solved "2141-maximum-running-time-of-n-computers". The links to the code solutions should also be updated to point to the actual files.
