# 88. Merge Sorted Array

## Problem Statement

You are given two integer arrays `nums1` and `nums2`, sorted in non-decreasing order. In addition, two integers `m` and `n` are provided, representing the number of elements in `nums1` and `nums2` respectively. 

The task is to merge `nums1` and `nums2` into a single array sorted in non-decreasing order. The final sorted array should be stored inside the array `nums1`. To accommodate this, `nums1` has a length of `m + n`, where the first `m` elements denote the elements that should be merged, and the last `n` elements are set to `0` and should be ignored. `nums2` has a length of `n`.

## Examples

**Example 1:**
```
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3

Output: [1,2,2,3,5,6]

The arrays we are merging are [1,2,3] and [2,5,6]. The result of the merge is [1,2,2,3,5,6].
```
**Example 2:**

Input: nums1 = [1], m = 1, nums2 = [], n = 0

Output: [1]

The arrays we are merging are [1] and []. The result of the merge is [1].

**Example 3:**

Input: nums1 = [0], m = 0, nums2 = [1], n = 1

Output: [1]

The arrays we are merging are [] and [1]. The result of the merge is [1]. Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.

## Constraints

- `nums1.length == m + n`
- `nums2.length == n`
- `0 <= m, n <= 200`
- `1 <= m + n <= 200`
- `-10^9 <= nums1[i], nums2[j] <= 10^9`
