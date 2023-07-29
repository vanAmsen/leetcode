class Solution {
    public List<List<Integer>> findDifference(int[] nums1, int[] nums2) {
        Set<Integer> set1 = Arrays.stream(nums1).boxed().collect(Collectors.toSet());
        Set<Integer> set2 = Arrays.stream(nums2).boxed().collect(Collectors.toSet());
        
        // Remove all elements from set1 that are present in set2
        set1.removeAll(Arrays.stream(nums2).boxed().collect(Collectors.toSet()));
        
        // Remove all elements from set2 that are present in set1
        set2.removeAll(Arrays.stream(nums1).boxed().collect(Collectors.toSet()));
        
        return Arrays.asList(new ArrayList<>(set1), new ArrayList<>(set2));
    }
}
