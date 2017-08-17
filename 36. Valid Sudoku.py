def isValidSudoku(self, board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    re = 1
    for i, row in enumerate(board):
        for j, c in enumerate(row):
