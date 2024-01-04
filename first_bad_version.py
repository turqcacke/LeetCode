def isBadVersion(k):
    return k >= 1383


class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n

        while right - left > 1:
            mid = (left + right) // 2
            bad = isBadVersion(mid)

            if bad:
                right = mid
            else:
                left = mid + 1

        return left if isBadVersion(left) else right


print(Solution().firstBadVersion(1500))
