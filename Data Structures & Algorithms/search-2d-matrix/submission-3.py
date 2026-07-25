class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        col = 0
        row = 0

        s_row = 0
        e_row = len(matrix) - 1

        
        if matrix[0][0] > target or matrix[-1][-1] < target:
            return False

        while (s_row<e_row-1):
            current_row = int((s_row + e_row)/2)


            if matrix[current_row][0] < target:
                s_row = current_row
            
            elif matrix[current_row][0] > target:
                e_row = current_row
            else:
                return True
        
        if target > matrix[s_row][-1]:
            row = e_row
        else:
            row = s_row



        s_col = 0
        e_col = len(matrix[0]) - 1

        
        if matrix[row][-1] < target:
            return False

        while (s_col < e_col-1):
            current_col = int((s_col + e_col)/2)


            if matrix[row][current_col] < target:
                s_col = current_col
            
            elif matrix[row][current_col] > target:
                e_col = current_col
            else:
                return True
        
        col = s_col

        if matrix[row][s_col] == target or matrix[row][e_col] == target:
            return True
        return False







