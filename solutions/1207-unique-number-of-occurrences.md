# 🧮 [VIDEO] 100% Unique Number of Occurrences 

# Intuition
When we first look at this problem, it becomes clear that we need to count the occurrences of each integer in the given array. A natural data structure that comes to mind for this task is a dictionary or a hash map, where we can use the integers as keys and their counts as values.

Once we have this count, we need to check if the number of occurrences for each integer is unique. One way to check the uniqueness of elements is by using a set, a data structure that automatically removes duplicates. 

https://youtu.be/uDE8ER8bb4E

# Approach
We start by creating a Counter object from the input array. This object, `count_dict`, is essentially a dictionary where the keys are the integers from the array and the values are their respective counts. 

Next, we extract the values from `count_dict` (i.e., the counts of the integers) and put them into a list, `count_values`.

Finally, we return whether the length of `count_values` is equal to the length of the set of `count_values`. If these lengths are equal, it means that all our counts are unique, so we return `True`. Otherwise, we return `False`.

# Complexity
- Time complexity: \(O(n)\), where \(n\) is the length of the input array. We have to iterate over the array once to count the occurrences of each integer, which takes linear time. 

- Space complexity: \(O(n)\), where \(n\) is the length of the input array. In the worst case scenario, all integers in the array are unique, so we would have to store each integer and its count in our dictionary. The space complexity is therefore linear in the size of the input.

This code solution is concise and efficient, leveraging Python's built-in data structures and libraries to solve the problem optimally.

# Code
``` Python []
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count_dict = Counter(arr)
        count_values = list(count_dict.values())
        return len(count_values) == len(set(count_values))
```
``` C++ []
class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        unordered_map<int, int> count;
        for (int num : arr) {
            count[num]++;
        }
        unordered_set<int> uniqueCount;
        for (auto& pair : count) {
            if (!uniqueCount.insert(pair.second).second) {
                return false;
            }
        }
        return true;
    }
};
```
``` Java []
class Solution {
    public boolean uniqueOccurrences(int[] arr) {
        Map<Integer, Integer> count = new HashMap<>();
        for (int num : arr) {
            count.put(num, count.getOrDefault(num, 0) + 1);
        }
        Set<Integer> uniqueCount = new HashSet<>(count.values());
        return uniqueCount.size() == count.size();
    }
}
```
``` JavaScript []
/**
 * @param {number[]} arr
 * @return {boolean}
 */
var uniqueOccurrences = function(arr) {
    let count = {};
    for (let num of arr) {
        if (num in count) {
            count[num]++;
        } else {
            count[num] = 1;
        }
    }
    let uniqueCount = new Set(Object.values(count));
    return uniqueCount.size === Object.keys(count).length;    
};
```
``` C# []
public class Solution {
    public bool UniqueOccurrences(int[] arr) {
        Dictionary<int, int> count = new Dictionary<int, int>();
        foreach (int num in arr) {
            if (count.ContainsKey(num)) {
                count[num]++;
            } else {
                count[num] = 1;
            }
        }
        HashSet<int> uniqueCount = new HashSet<int>(count.Values);
        return uniqueCount.Count == count.Count;
    }
}
```
