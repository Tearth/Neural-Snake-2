# Neural Snake 2
Second version of program which learns how to play Snake game using neural networks and genetic/evolutionary algorithms. Learning process is divided to generations, where every one contains 10 games. A few of neural networks with the highest scores are selected to breeding. After +-50 generations, the snake is capable to play without colliding with the wall and eat multiple feeds.

![example screenshot](https://i.imgur.com/gyL7vhE.gif)

# Neural network parameters
**Input** (1 = yes, -1 = no):
  * is top available to move
  * is right available to move
  * is bottom available to move
  * is left available to move
  * is food above snake
  * is food to the right of snake
  * is food under snake
  * is food to the left of snake

**Output** ([-1, 1]):
  * move top
  * move right
  * move down
  * move left

# Used libraries:
  * **TensorFlow**: neural networks stuff