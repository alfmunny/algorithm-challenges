import unittest

class BoardSolution:

  def __init__(self, board, color):
    self.original_board = board
    self.board = [ [ x for x in row ] for row in board ] 
    self.n = len(board)
    self.color = color
    self.max_tiles = 0
    self.move = 0
    self.memo = []
    self.see_output = False

  def reset(self):
    self.board = [ [ x for x in row ] for row in self.original_board ] 
    self.memo = []
    self.max_tiles = 0
    self.move = 0

  def play(self):
    self.reset()
    choosen_color = self.color[0]

    while True:
      current_max = 0
      for color in self.color:
        if color == self.board[0][0]:
          continue

        self.count_tiles(0, 0, color)

        if self.max_tiles > current_max:
          current_max = self.max_tiles
          choosen_color = color

      if self.max_tiles == self.n * self.n:
        break

      self.move += 1
      self.flood(0, 0, self.board[0][0], choosen_color)

      if self.see_output:
        self.print(self.board)

    return self.move

  def count_tiles(self, i, j, color):
    self.max_tiles = 0
    self.memo = [ [0]*self.n for i in range(self.n) ] 
    self.dfs(0, 0, self.board[i][j], color)
    return self.max_tiles

  def flood(self, i, j, original_color, color):
    board = self.board
    n = self.n
    if i >= n or i < 0 or j >= n or j < 0 or board[i][j] == color:
      return board

    if board[i][j] == original_color:
      board[i][j] = color
      self.flood(i+1, j, original_color, color)
      self.flood(i, j+1, original_color, color)
      self.flood(i-1, j, original_color, color)
      self.flood(i, j-1, original_color, color)
    return board

  def dfs(self, i, j, original_color, color):
    board = self.board
    n = len(board)
    if i >= n or i < 0 or j >= n or j < 0 or self.memo[i][j]:
      return

    if board[i][j] == color or board[i][j] == original_color:
      if board[i][j] == color:
        original_color = color
      self.memo[i][j] = 1
      self.max_tiles += 1
      self.dfs(i+1, j, original_color, color)
      self.dfs(i, j+1, original_color, color)
      self.dfs(i-1, j, original_color, color)
      self.dfs(i, j-1, original_color, color)


  def print(self, board):
    print("========= Move ", self.move)
    for row in board:
      print(row)
    print("==============")

  def allow_print(self, value=True):
    self.see_output = value


class BoardSolutionTest(unittest.TestCase):

  board0 = [
      [1, 1, 1, 1, 1, 1],
      [1, 1, 1, 1, 1, 1],
      [1, 1, 1, 1, 1, 1],
      [1, 1, 1, 1, 1, 1],
      [1, 1, 1, 1, 1, 1],
      [1, 1, 1, 1, 1, 1],
      ]

  board1 = [
      [0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 1, 0],
      ]

  board2 = [
      [2, 2, 2, 2, 2, 2],
      [2, 0, 2, 2, 2, 2],
      [2, 0, 2, 2, 2, 2],
      [2, 0, 2, 0, 2, 2],
      [2, 0, 2, 0, 2, 2],
      [2, 0, 2, 2, 1, 2]]

  board3 = [
      [0, 1, 2, 3, 6, 4],
      [1, 0, 2, 7, 8, 3],
      [1, 0, 2, 3, 8, 3],
      [1, 0, 2, 0, 2, 3],
      [1, 0, 5, 0, 2, 3],
      [1, 0, 2, 4, 1, 8],
      ]

  color = [0, 1, 2, 3, 4, 5, 6, 7, 8]
  
  def test_count_tiles(self):
    sol1 = BoardSolution(self.board1, self.color)
    sol2 = BoardSolution(self.board2, self.color)
    self.assertEqual(sol1.count_tiles(0, 0, 1), 36)
    self.assertEqual(sol1.count_tiles(0, 0, 2), 35)
    self.assertEqual(sol2.count_tiles(0, 0, 0), 35)

  def test_flood(self):
    sol1 = BoardSolution(self.board1, self.color)
    sol2 = BoardSolution(self.board2, self.color)
    self.assertEqual(sol2.flood(0, 0, 2, 0), self.board1)
    self.assertEqual(sol1.flood(0, 0, 0, 1), self.board0)

  def test_play(self):
    sol0 = BoardSolution(self.board0, self.color)
    sol1 = BoardSolution(self.board1, self.color)
    sol2 = BoardSolution(self.board2, self.color)
    sol3 = BoardSolution(self.board3, self.color)
    self.assertEqual(sol0.play(), 0)
    self.assertEqual(sol1.play(), 1)
    self.assertEqual(sol2.play(), 2)
    self.assertEqual(sol3.play(), 12)


if __name__ == '__main__':
# Let's run some the unit tests
  unittest.main(verbosity=2)

