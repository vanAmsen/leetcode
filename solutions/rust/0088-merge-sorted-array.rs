impl Solution {
    pub fn merge(nums1: &mut Vec<i32>, m: i32, nums2: &mut Vec<i32>, n: i32) {
        let (mut p1, mut p2) = (m as usize, n as usize);
        
        while p2 > 0 {
            if p1 > 0 && nums1[p1 - 1] > nums2[p2 - 1] {
                nums1[p1 + p2 - 1] = nums1[p1 - 1];
                p1 -= 1;
            } else {
                nums1[p1 + p2 - 1] = nums2[p2 - 1];
                p2 -= 1;
            }
        }
    }
}
