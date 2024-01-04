class Solution():

    def __init__(self):
        self.combs = set()
        self.m = None

    def find_n(self, n: int) -> tuple[int, int]:
        n_list = list()
        queue = list()
        self.m = n

        while n != 0:
            n_list.append(n % 10)
            n = n // 10

        for i in range(len(n_list)):
            queue.append(
                (n_list[i], n_list[0:i] + n_list[i+1::])
            )

        while len(queue) > 0:
            current_comb = queue.pop(0)
            num = current_comb[0]

            self.combs.add(num)
            self.m = self.m if self.m > num else num

            for i in range(len(current_comb[-1])):
                queue.append((num * 10 + current_comb[-1][i], current_comb[-1][0:i] + current_comb[i+!]))

        return (self.m, len(self.combs))


print(Solution().find_n(n=111))
print(Solution().find_n(n=0))
print(Solution().find_n(n=121))
print(Solution().find_n(n=6630))
