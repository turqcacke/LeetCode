from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        pixels_store = set()
        ignore_store = set()

        max_row = len(image)
        max_col = len(image[0])

        starting_color = None

        if sc < max_col and sc >= 0 and sr < max_row and sr >= 0:
            pixels_store.add((sr, sc))
            starting_color = image[sr][sc]

        while pixels_store:
            current_node = pixels_store.pop()
            ignore_store.add(current_node)

            row = current_node[0]
            column = current_node[1]

            if image[row][column] == starting_color:
                image[row][column] = color

            connected_points = (
                (row + 1, column),
                (row-1, column),
                (row, column + 1),
                (row, column - 1)
            )
            for point in connected_points:
                if point in ignore_store:
                    continue
                elif (
                    point[0] >= 0
                    and point[1] >= 0
                    and point[0] < max_row
                    and point[1] < max_col
                    and image[point[0]][point[1]] == starting_color
                ):
                    pixels_store.add(point)

        return image


print(Solution().floodFill(
    image=[[0, 0, 0], [1, 0, 0]], sr=1, sc=0, color=2))
