# Path Finding Visualisation
Very simply program I made because I was bored. Shows you the thought process of the computer during path finding. I did BFS, DFS and A* (I didn't bother with Dijkstra's as all weights are the same - 1 for one cell, and so this would be the same as BFS). <br>
To run just call:
```
python visualise.py <algorithm>
```
Where `algorithm` is one of `BFS`, `DFS` or `AStar`. <br>
Left click to add walls, right click to remove walls. You can press the space bar to start and pause the path finding. While paused you can also add extra blocks if it is on a cell that has not yet been visited. <br>
Enjoy :)