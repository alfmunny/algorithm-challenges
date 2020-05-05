# Color Fill

We have a board of N * N, a set of colors M.

Every time you can pick a new color from M to paint on the origin at index [0][0], the color will flood the tiles, which have the same color as the color of the origin.

How we can minimize the steps we take to paint the whole board with same color.

Naive solution: Greedy Solution

1. Pick a color
2. Do DFS from the origin with that color, count out the max tiles. Repeat step 1 until all color has been tried.
3. Use the color with the maximum number of tiles, flood the board.
4. Repeat step 1 until all the tiles are the same color.

Possible improvements:

- Step 2 can be optimized: 
  - We can remember the 'front line' of the painted region, and do DFS from the line, not always from the origin. 
  - How can we draw the 'font line' of the region faster

## Run 

```shell
python color-fill.py
```

Result
```
test_count_tiles (__main__.BoardSolutionTest) ... ok
test_flood (__main__.BoardSolutionTest) ... ok
test_play (__main__.BoardSolutionTest) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.014s
```
