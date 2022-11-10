from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = -1
        for i in range(len(nums)):
            if nums[i] != 0:
                left += 1
                nums[left], nums[i] = nums[i], nums[left]
        return nums

if __name__ == "__main__":
    s = Solution()
    nums = [1, 0, 3, 5, 0, 6]
    output = s.moveZeroes(nums)
    print(output)
