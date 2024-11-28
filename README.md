# What is a nonogram?

A nonogram is a logic puzzle on a grid, where based on “clues” in the form of numbers at the top of columns and the left of rows, the player must use a set of procedures to find what cells should be filled in with a specific color. Below is an example of a nonogram of a fish, where only one color is used.

![image](https://github.com/user-attachments/assets/d9e61f3c-df71-43c1-8cd9-81f65310383b)

Some simple procedures to solve nonograms include line logic and edge logic. Line logic involves analyzing a single line, that is a column or row, and visualizing all possible ways that the line can be filled based on the clue. If in all scenarios a cell must be filled with a certain color, then the player can fill those cells. Information from this cell can provide clues as to how other lines can be filled. This is the basis of the game. 

Edge logic involved assessing a line that appears on the border of the grid. If the player can place color along an edge, then the player can identify information about the adjacent line.

Nonograms of multiple colors function slightly differently than those of only one. If 2 different colors are in a clue, then there is no requirement for a blank cell to separate them. 

![image](https://github.com/user-attachments/assets/dbb7367b-772e-4e31-b269-b30ae0a9b99c)

Since blank cells provide the ambiguity of grids, more colors could potentially lead to less ambiguity.

More complex solving techniques exist, but present difficult games when they are required. For the sake of this experiment, we declare these grids as poorly designed.

# What do solvability and uniqueness mean?

A nonogram is considered solvable if there is any non-zero number of ways to fill in the grid given the specified clues. Grids aren’t solvable if the sum of the clues on top and bottom are not equal. Even if they are equal, this does not necessarily mean that the grid is solvable. See the image below.

![image](https://github.com/user-attachments/assets/da89e7f9-0628-4354-b568-8c33567ccda8)

A nonogram is considered unique if there exists exactly one possible way to fill a grid based on the instructions. Many nonograms contain elementary switching components, or sections of clues that are ambiguous and no advanced solving technique can solve. To complete the puzzle, the player is required to guess at random. An example of a basic switching component is given below.

![image](https://github.com/user-attachments/assets/415c76a5-bedb-4172-803d-6e6643fe0dc7)

This is widely viewed as a poorly designed puzzle.

# What is the objective of this project?

This project ultimately aims to uncover how many nonograms are unique considering size of grids and number of colors present. This repository applies the principle of inclusion-exclusion to count how many ways a grid can be filled. By definition all counted grids are solvable, however uniqueness is not accounted for. This code establishes an upper bound to how many unique grids are possible, however more advanced computation is necessary to find uniqueness.

# Results?

The data shows that around approximately 72% of all possible colors being present on the grid, the greatest number of grids are possible. 

![image](https://github.com/user-attachments/assets/cd5d76d0-594f-40a8-8ded-9b0a876ec6e3)

A modification of this program reveals the integer sequence of each iteration. Interestingly, this pattern is reflected in the On-Line Encyclopedia of Integer Sequences in A053440 and appears to form Worpitzky’s Triangle. 

# Why nonograms?

Nonograms present a visual example of combinatorial identities. Discrete tomography has potential applications to cybersecurity in how to encode pixels of an image. Also, because nonograms are fun!

# What next?

More detailed descriptions of findings can be found in conclusions.pdf. To uncover exactly how many grids are unique, I plan on creating a nonogram game that randomly generates a puzzle “key” that dictates what cells are to be filled each color. Then, the program will extract the clues based on the final puzzle and attempt to solve the grid. If the grid can be successfully solved by an algorithm that doesn’t require guessing, we flag the puzzle as unique. If it cannot be solved, we flag it as not unique. Because we start by passing a complete puzzle, we know all are solvable. Exact statistical methods to count these grids and how to handle puzzles that require advanced solving techniques are yet to be determined.
