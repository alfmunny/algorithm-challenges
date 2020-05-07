# Color Fill

Problem hidden :)

## Solution
Naive solution:

1. Pick a color
2. Do DFS from the origin with that color, count out the max tiles. Repeat step 1 until all color has been tried.
3. Use the color with the maximum number of tiles, flood the board.
4. Repeat step 1 until all the tiles are the same color.

Possible improvements:

- Step 2 can be optimized: 
  - We can remember the 'front line' of the painted region, and do DFS from the line, not always from the origin. 
  - We can only pick the color which are adjusted to the front line
  - How can we draw the font line of the region faster

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

## A small application

I wrote a application to demonstrate this problem.

[Color Flood Fill](http://alfmunny.com/algorithm-challenges/color-fill/)


