# Problem Understanding

In the "Sliding Window Maximum" problem, we are given an array of integers `nums` and an integer `k` representing the size of the sliding window. The task is to determine the maximum value in each sliding window as it moves from the beginning to the end of the array.

For instance, given the array  \text{nums} = [1,3,-1,-3,5,3,6,7]  and  k = 3 , the output should be $$[3,3,5,5,6,7]$$.

**Input**: nums = $$[1,3,-1,-3,5,3,6,7]$$, $$k = 3$$
**Output**: $$[3,3,5,5,6,7]$$

---

# Live Coding in Python:
https://youtu.be/liObQND4xI8

# Approach: Deque for Maintaining Sliding Window Maximum

To solve the "Sliding Window Maximum" problem, we leverage the power of a double-ended queue (often referred to as `deque`). This structure is vital because it efficiently keeps track of the maximum value in the current sliding window while iterating through the list.

## Key Data Structures:
- **Array**: This is the input `nums` that represents the series of numbers we're working with.
- **Deque**: A double-ended queue that provides quick access to both its ends. Here, it will hold indices of the `nums` array elements, not the actual numbers.

## Enhanced Breakdown:

1. **Initialization**:
   - Set up the primary structures: an empty `deque` named `deq` for indexing and tracking, and a list named `result` to collect the maximum values from each window.

2. **Processing Each Element**:
   - Progressively traverse the array `nums`.
   - For each number at index `i`:
     - **Pruning Outdated Indices**: Examine the front of the `deq`. If the index it holds is no longer within the range of the current window, discard it. This keeps our window up-to-date.
     - **Deque Maintenance for Maximum**: As we encounter each number, eliminate indices from the deque's rear if the numbers they reference in `nums` are outclassed by the current one. This process guarantees that the deque's front always indicates the current window's champion.
     - **Storing Current Index**: Register the current index `i` at the tail of the `deq`.
     - **Harvesting Results**: Once we've traversed at least `k` numbers (and thus our window is fully operational), the deque's front will pinpoint the maximum number's index for the current window. Extract this number from `nums` and deposit it into our `result`.

3. **Wrap-up**:
   - Post traversal, the `result` list will be populated with the peak values from each window, and this becomes our solution.

Leveraging the `deque` in this manner turns a potentially intricate problem into a manageable and efficient task, demonstrating the power of the right data structure in problem-solving.

## Example:

Given the array $$ \text{nums} = [1,3,-1,-3,5,3,6,7] $$ and $$ k = 3 $$:

The deque evolves as follows:

![c3e830e5-3ab7-46fb-8527-b725aedece94.png](https://assets.leetcode.com/users/images/3ab17193-1445-4a9b-b940-7acbd03ed9cf_1692151958.8833754.png)

1. After processing `1`: 
   - deq = [0] (indices of 1 in nums)
2. After processing `3`: 
   - Removed rightmost element from deq since the current number is larger.
   - deq = [1] (indices of 3 in nums)
3. After processing `-1`: 
   - deq = [1, 2] (indices of 3, -1 in nums)
   - result = [3]
4. After processing `-3`: 
   - deq = [1, 2, 3] (indices of 3, -1, -3 in nums)
   - result = [3, 3]
5. After processing `5`: 
   - Removed leftmost element from deq because it's out of the current window.
   - Removed rightmost element from deq since the current number is larger (twice).
   - deq = [4] (indices of 5 in nums)
   - result = [3, 3, 5]
6. After processing `3`: 
   - deq = [4, 5] (indices of 5, 3 in nums)
   - result = [3, 3, 5, 5]
7. After processing `6`: 
   - Removed rightmost element from deq since the current number is larger (twice).
   - deq = [6] (indices of 6 in nums)
   - result = [3, 3, 5, 5, 6]
8. After processing `7`: 
   - Removed rightmost element from deq since the current number is larger.
   - deq = [7] (indices of 7 in nums)
   - result = [3, 3, 5, 5, 6, 7]

This breakdown provides a step-by-step visualization of how the deque and the result list evolve as the function processes each number in the array.

# Complexity:

**Time Complexity:** $$ O(n) $$
- We traverse the array once, making the time complexity linear in the size of the array.

**Space Complexity:** $$ O(k) $$
- We use a deque that can hold at most `k` indices.

# Performance:

Given the constraints, this solution is optimal and will efficiently handle arrays of size up to $$ 10^5 $$ elements.

| Language  | Runtime (ms) | Runtime Beat (%) | Memory (MB) | Memory Beat (%) |
|-----------|--------------|------------------|-------------|-----------------|
| Java      | 30           | 87.28%           | 59.6        | 63.2%           |
| Rust      | 53           | 97.64%           | 3.4         | 58.27%          |
| C++       | 200          | 91.18%           | 134.8       | 36.59%          |
| Go        | 210          | 92.52%           | 9.8         | 60.66%          |
| C#        | 398          | 84.61%           | 64.9        | 40.83%          |
| JavaScript| 613          | 65.33%           | 91.7        | 35.36%          |
| Python3   | 1327         | 87.77%           | 33.1        | 64.19%          |

![perf_239.png](https://assets.leetcode.com/users/images/92e4e176-ad8e-4100-a258-8d457ce15edc_1692147821.533873.png)


# Code
``` Python []
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []
        if k == 1:
            return nums
        
        deq = deque()
        
        result = []
        for i in range(len(nums)):
            while deq and deq[0] < i - k + 1:
                deq.popleft()
            while deq and nums[i] > nums[deq[-1]]:
                deq.pop()
            
            deq.append(i)
            if i >= k - 1:
                result.append(nums[deq[0]])
        
        return result
```
``` C++ []
class Solution {
public:
    std::vector<int> maxSlidingWindow(std::vector<int>& nums, int k) {
        if (nums.empty() || k == 0) {
            return {};
        }
        if (k == 1) {
            return nums;
        }

        std::deque<int> deq;
        std::vector<int> result;

        for (int i = 0; i < nums.size(); ++i) {
            while (!deq.empty() && deq.front() < i - k + 1) {
                deq.pop_front();
            }
            while (!deq.empty() && nums[i] > nums[deq.back()]) {
                deq.pop_back();
            }
            
            deq.push_back(i);
            if (i >= k - 1) {
                result.push_back(nums[deq.front()]);
            }
        }
        
        return result;
    }
};
```
``` Go []
func maxSlidingWindow(nums []int, k int) []int {
    if len(nums) == 0 || k == 0 {
        return []int{}
    }
    if k == 1 {
        return nums
    }

    var deq []int
    var result []int

    for i := 0; i < len(nums); i++ {
        for len(deq) > 0 && deq[0] < i - k + 1 {
            deq = deq[1:]
        }
        for len(deq) > 0 && nums[i] > nums[deq[len(deq)-1]] {
            deq = deq[:len(deq)-1]
        }

        deq = append(deq, i)
        if i >= k - 1 {
            result = append(result, nums[deq[0]])
        }
    }
    
    return result
}
```
``` Java []
public class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        if (nums == null || nums.length == 0 || k == 0) {
            return new int[0];
        }
        if (k == 1) {
            return nums;
        }

        Deque<Integer> deq = new LinkedList<>();
        int[] result = new int[nums.length - k + 1];

        for (int i = 0; i < nums.length; i++) {
            while (!deq.isEmpty() && deq.peek() < i - k + 1) {
                deq.poll();
            }
            while (!deq.isEmpty() && nums[i] > nums[deq.peekLast()]) {
                deq.pollLast();
            }

            deq.offer(i);
            if (i >= k - 1) {
                result[i - k + 1] = nums[deq.peek()];
            }
        }
        
        return result;
    }
}
```
``` JavaScript []
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var maxSlidingWindow = function(nums, k) {
    if (!nums.length || k === 0) {
        return [];
    }
    if (k === 1) {
        return nums;
    }

    let deq = [];
    let result = [];

    for (let i = 0; i < nums.length; i++) {
        while (deq.length && deq[0] < i - k + 1) {
            deq.shift();
        }
        while (deq.length && nums[i] > nums[deq[deq.length - 1]]) {
            deq.pop();
        }

        deq.push(i);
        if (i >= k - 1) {
            result.push(nums[deq[0]]);
        }
    }
    
    return result;
};
```
``` C# []
public class Solution {
    public int[] MaxSlidingWindow(int[] nums, int k) {
        if (nums == null || nums.Length == 0 || k == 0) {
            return new int[0];
        }
        if (k == 1) {
            return nums;
        }

        LinkedList<int> deq = new LinkedList<int>();
        List<int> result = new List<int>();

        for (int i = 0; i < nums.Length; i++) {
            while (deq.Count > 0 && deq.First.Value < i - k + 1) {
                deq.RemoveFirst();
            }
            while (deq.Count > 0 && nums[i] > nums[deq.Last.Value]) {
                deq.RemoveLast();
            }

            deq.AddLast(i);
            if (i >= k - 1) {
                result.Add(nums[deq.First.Value]);
            }
        }
        
        return result.ToArray();
    }
}
```
``` Rust []
use std::collections::VecDeque;

impl Solution {
    pub fn max_sliding_window(nums: Vec<i32>, k: i32) -> Vec<i32> {
        if nums.is_empty() || k == 0 {
            return vec![];
        }
        if k == 1 {
            return nums;
        }

        let mut deq = VecDeque::new();
        let mut result = Vec::with_capacity(nums.len() - k as usize + 1);

        for i in 0..nums.len() {
            // This is equivalent to: while deq and deq[0] < i - k + 1
            while let Some(&front) = deq.front() {
                if front < i as i32 - k + 1 {
                    deq.pop_front();
                } else {
                    break;
                }
            }

            // This is equivalent to: while deq and nums[i] > nums[deq[-1]]
            while let Some(&back) = deq.back() {
                if nums[i] > nums[back as usize] {
                    deq.pop_back();
                } else {
                    break;
                }
            }

            deq.push_back(i as i32);

            if i as i32 >= k - 1 {
                result.push(nums[*deq.front().unwrap() as usize]);
            }
        }

        result
    }
}
```

This problem beautifully showcases the power and elegance of the sliding window technique. Embracing the right data structures, like the deque in this scenario, can turn complex challenges into tractable ones. Journey through the terrains of algorithms, welcome every challenge, and remember that every complexity you unravel strengthens your algorithmic acumen. Remain passionate, continue coding, and relish every step of your coding odyssey! 💡🌠👩‍💻👨‍💻
