from collections import deque
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        d = deque(nums)
        while (i < k):
            temp = d.pop()
            d.appendleft(temp)
            i += 1
        nums[:] = d
        return nums

if __name__ == "__main__":
    s = Solution()
    nums = [1,2,3,4,5,6,7]
    target = 3
    output = s.rotate(nums, target)
    print(output)