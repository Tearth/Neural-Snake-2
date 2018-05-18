# NeuralSnake 2
Second version of program which learns how to play Snake game using neural networks and genetic/evolutionary algorithms. Learning process is divided to generations, where every one contains 10 games. A few of neural networks with the highest scores are selected to breeding. After +-50 generations, snake is capable to play without colliding with the wall and eat multiple feeds.

![example screenshot](https://nooq9g.db.files.1drv.com/y4mjBAYt4FdDukrN-M87TD2DuZhwIdPYDemFjMDxkx9K0LGPTY9h3b78bOv5tbtqyK3t3L66Fdk1fAw5H3khVOoi2IGv1hXttdqq_z61H-HrhFj7fmTliCTGx87EOfXKjCo_6Ge5MEEf0ejpzNazkVWqOBoZDGiSpc76TFuPkBX5brY9v-1tBsEQ5j1jkT41krH04-Zx34jM4O-S4CyzgFhtdJMh6FRlPxpTpWHLx-EJRI/snake2.gif)

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