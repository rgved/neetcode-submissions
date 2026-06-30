class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        large=len(matrix)
        small=len(matrix[0])

        l=0
        r=large*small-1
        while l<=r:
            m=(l+r)//2
            row=m//small
            col=m%small

            if target<matrix[row][col]:
                r=m-1
            elif target>matrix[row][col]:
                l=m+1
            else:
                return True
        return False
