class Solution:
    def getRow(self, rowIndex: int):
        row = [1]

        prev = 1

        for r in range(1, rowIndex + 1):
            current = prev * (rowIndex - r + 1) // r
            row.append(current)
            prev = current

        return row