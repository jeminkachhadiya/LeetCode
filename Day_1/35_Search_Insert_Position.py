from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i]>= target:
                return i
        return n

if __name__ == "__main__":
    s = Solution()
    nums = [1, 3, 5, 6]
    target = 5
    output = s.searchInsert(nums, target)
    print(output)