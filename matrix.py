from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        pos_list = []
        visited_positions = set()

        directions = (
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
        )

        for i in range(len(mat)):
            row = mat[i]
            for j in range(len(row)):
                if row[j] == 0:
                    pos_list.append((i, j, 0))

        while pos_list:
            pos = pos_list.pop(0)
            pos_val = mat[pos[0]][pos[1]]
            visited = (pos[0], pos[1]) in visited_positions

            if pos_val != 0 and not visited:
                mat[pos[0]][pos[1]] = pos[-1]
            if not visited:
                for d in directions:
                    r = d[0] + pos[0]
                    c = d[1] + pos[1]
                    if r < len(mat) and r >= 0 and c < len(mat[0]) and c >= 0 and mat[r][c] != 0:
                        pos_list.append(
                            (r, c, pos[-1] + 1)
                        )
            else:
                continue
            visited_positions.add((pos[0], pos[1]))

        return mat


print(Solution().updateMatrix([[1, 1, 1, 1, 1], [1, 0, 1, 1, 1], [
      1, 1, 1, 0, 1], [0, 1, 0, 1, 1], [1, 1, 1, 1, 1]]))
print(Solution().updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]]))
print(Solution().updateMatrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
