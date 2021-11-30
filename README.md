# Apollo-and-Diana-maze-

# Introduction
This project requires you to model the problem below as a graph and then use a known graph
algorithm to solve the problem.
You must traverse a field of arrows (red or blue). You must find a route from the arrow in the
top left corner to the bullseye in the bottom right corner. You must follow the direction that the
arrows point, and you can only stop on the other colored arrow or the bullseye. For example, start
on red, then chose a blue arrow (in the direction that the red arrow is pointing), then from the blue
arrow chose a red arrow in the direction the blue arrow is pointing. Continue in this fashion until
you find the bullseye in the bottom right corner. It does not have to be the first opposite color that
you find. You may find your-self in a loop and continuously visiting the same arrows; you need
to account for this. You must find the correct path. You also need to handle what happens if you
get to a node that you already visited within a path and you need to continue in that direction

# Input file format
Your program should read its input from a file with the following format. The input begins with
two positive characters on a line indicating the number of rows r and columns c of the maze, respectively. The next r lines contain the color and directional information for each arrow in the
maze. Each line has c values, where each value represents the color of the arrow by the direction of the arrow (N, E, S, W, NE, SE, SW, or NW). The color codes R and B represent red and
blue, respectively, while the direction codes represent north, east, south, west, northeast, southeast, southwest, or northwest, respectively. The bulls-eye is represented by the letter O. You may

# Sample input file

![image](https://user-images.githubusercontent.com/65825453/143988371-eee0ac50-e8bc-4c8c-8d7d-a49af1130aa0.png)

# Output file format
You must write the output file in the following format. The output will consist of a path from the
top left square to the bottom right square (bulls-eye). Write a single line consisting of a sequence of
moves, separated by spaces. Each move should be represented by the number of spaces to move
and the direction, with no spaces in between. The direction should be represented using N, E, S,
W, NE, SE, SW, and NW, as in the input. The sequence of moves must solve the maze from the
input. For example, if your first 3 moves take you 3 spaces east, 3 spaces southwest, and 4 spaces
southeast, your output should begin as follows (note, the 3 moves below correspond to the first
three possible moves to the graph in Figure 1): 3E 3SW 4SE
You will be given multiple mazes to test, along a script that you can use to determine if your
solution is correct. The output file must follow a particular naming convention: input file namesoln.txt (see example below). The script to test your solutions is verifyGraph.py. This script takes
two command line parameters: (1) the input graph; and (2) and your solution file. See below for
an example of running it.
python verifyGraph.py small.txt small-soln.txt
