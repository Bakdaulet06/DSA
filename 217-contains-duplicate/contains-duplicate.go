func containsDuplicate(nums []int) bool {
    m := make(map[int]bool)
    for i := range nums{
        if m[nums[i]] {
            return true
        }
        m[nums[i]] = true
    }
    return false
}