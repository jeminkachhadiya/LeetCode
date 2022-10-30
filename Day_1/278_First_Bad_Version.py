# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n == 1: return 1;
        beg = 1
        end = n
        while beg < end:
            mid = beg + (end - beg)//2
            if isBadVersion(mid): end=mid
            else: beg = mid + 1
        return beg


# if __name__ == "__main__":
#     print(Solution.firstBadVersion(Solution, 10))

