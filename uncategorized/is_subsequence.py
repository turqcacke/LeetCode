class Solution:
    def climbStairs(self, n: int) -> int:
        arr = [0, 1, 2]

        for i in range(3, n + 1):
            arr.append(arr[i - 1] + arr[i - 2])
        return arr[i]


print(Solution().climbStairs(3))
