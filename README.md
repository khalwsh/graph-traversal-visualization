# Pathfinding Visualization using Pygame

This project visualizes the pathfinding algorithms BFS (Breadth-First Search) and DFS (Depth-First Search) using Pygame. It allows users to interactively place start and end points, as well as obstacles, and then visualize the pathfinding process.

## Features

- **Grid-based Visualization**: A 20x20 grid where each cell can be a start point, end point, obstacle, or part of the path.
- **Interactive Interface**: Place the start and end points, and obstacles by clicking on the grid.
- **Two Pathfinding Algorithms**: Choose between BFS and DFS to find the shortest path.
- **Start Menu**: Simple start menu to choose the algorithm.

## Controls

- **Left Click**: 
  - Place the start point (yellow) and end point (blue).
  - Place obstacles (black) after the start and end points are set.
- **Right Click**: Remove the start point, end point, or obstacles.
- **Spacebar**: Run the selected pathfinding algorithm (BFS or DFS).

## Getting Started

### Prerequisites

- Python 3.x
- Pygame library

### Installation

install the required Python packages
```sh
pip install pygame
```
3.running the program
```sh
python3 main.py
```
## How to Use
- Run the script to open the pygame window
- in the start menu, click on "DFS" or "BFS" to choose the algorithm
- click on the grid to set the start point(yellow) and the end point (blue)
- click on the grid to set obstacles(black)
- press the spacebar to run the chosen algorithm after setting up the above steps