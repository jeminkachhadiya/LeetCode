from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l, r = 0, n-1
        res = [0] * n
        index = n - 1
        while(l<=r):
            if abs(nums[l]) < abs(nums[r]):
                res[index] = nums[r] ** 2
                r -= 1
            else:
                res[index] = nums[l] ** 2
                l += 1
            index -= 1
        return res


if __name__ == "__main__":
    s = Solution()
    nums = [1, -3, 5, 6]
    output = s.sortedSquares(nums)
    print(output)