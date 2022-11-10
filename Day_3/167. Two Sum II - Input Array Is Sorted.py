from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers) - 1
        i = 0
        while (i < n):
            if numbers[i] + numbers[n] < target:
                i += 1
            elif numbers[i] + numbers[n] > target:
                n -= 1
            else:
                return i + 1, n + 1


if __name__ == "__main__":
    s = Solution()
    nums = [1,2,3,4,5,6,7]
    target = 11
    output = s.twosum(nums, target)
    print(output)