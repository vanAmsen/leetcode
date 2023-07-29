# 🔢🔍 Find the Difference of Two Arrays

# Intuition

Our first thoughts on solving this problem revolve around the concept of set differences. Given two integer arrays, we need to find the unique integers in the first array that are not in the second, and vice versa. The idea of set difference fits perfectly here. 

# Approach

We approach this problem by leveraging the capabilities of Python sets. Here are the steps:

1. Convert the input lists to sets. This serves two purposes: it removes any duplicate elements, and it allows us to perform set operations. 

2. Use the `-` operator to find the difference between the sets. This gives us the elements that are in one set but not in the other.

3. Convert the resulting sets back to lists and return them.

# Complexity

- Time complexity: The time complexity of our solution is \(O(n)\), where \(n\) is the length of the longer input list. This is because we iterate through each list once to convert it to a set.

- Space complexity: The space complexity of our solution is also \(O(n)\), where \(n\) is the length of the longer input list. This is because we create a new set for each input list.

# Code

```python
from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        diff1 = set1 - set2
        diff2 = set2 - set1
        return [list(diff1), list(diff2)]
```

This Python code defines a function `findDifference` that finds and returns the difference between two input arrays. The function is part of a class `Solution`, as required by the LeetCode problem format.
