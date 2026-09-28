board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# def solve(board: list[list[str]]) -> None:
#         """
#         Do not return anything, modify board in-place instead.
#         """
#         m=len(board)
#         n=len(board[0])
#         for i,a in enumerate(board):
#             if i!=0 and i!=m-1:
#                 for j,b in enumerate(a):
#                     if j!=0 and j!=n-1:
#                         if b=='O':
#                             board[i][j]='X'
# solve(board)
# print(board)
m=len(board)
n=len(board[0])
# def dfs(i,j):
#     if i<0 or i>=m or j<0 or j>=n:
#         return
#     if board[i][j]=='X':
#         return
#     board[i][j]='S'
#     dfs(i+1,j)
#     dfs(i-1,j)
#     dfs(i,j+1)
#     dfs(i,j-1)
# for i in range(m):
#     for j in range(n):
#         if board[i][j] and (i in [0,m-1] or j in [0,n-1]):
#             dfs(i,j)
# for i in range(m):
#     for j in range(n):
#         if board[i][j]=='O':
#             board[i][j]='X'
#         if board[i][j]=='S':
#             board[i][j]="O"
class Solution:
    def solve(self,board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m=len(board)
        n=len(board[0])
        def dfs(i,j):
            stack=[(i,j)]
            while stack:
                r,c=stack.pop()
                if (r<0 or r>=m or c<0 or c>=n) or board[r][c]!="O":
                    continue
                board[r][c]="S"
                stack.extend([(r-1,c),(r+1,c),(r,c-1),(r,c+1)])
        for i in range(m):
            for j in range(n):
                if board[i][j]=="O" and (i in [0,m-1] or j in [0,n-1]):
                    dfs(i,j)
        for i in range(m):
            for j in range(n):
                if board[i][j]=='O':
                    board[i][j]='X'
                if board[i][j]=='S':
                    board[i][j]="O"
print(board)