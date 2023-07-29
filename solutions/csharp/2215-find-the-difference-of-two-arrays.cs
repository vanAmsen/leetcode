public class Solution {
    public IList<IList<int>> FindDifference(int[] nums1, int[] nums2) {
        HashSet<int> set1 = new HashSet<int>(nums1);
        HashSet<int> set2 = new HashSet<int>(nums2);
        
        set1.ExceptWith(nums2);
        set2.ExceptWith(nums1);
        
        return new List<IList<int>> { set1.ToList(), set2.ToList() };
    }
}
