class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        r = len(matrix)
        c = len(matrix[0])

        top = 0
        bottom = r - 1
        left = 0
        right = c - 1

        result = []

        while top <= bottom and left <= right:

            # 1. Left to right
            for j in range(left, right + 1):
                result.append(matrix[top][j])
            top += 1

            # 2. Top to bottom
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            # 3. Right to left
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    result.append(matrix[bottom][j])
                bottom -= 1

            # 4. Bottom to top
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result