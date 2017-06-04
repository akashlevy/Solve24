# Solve24
Solves the game 24 using brute force

## How to play 24
Given a 4-digit number, manipulate the numbers using the allowed operations to come to 24.

Allowed operations: addition, subtraction, multiplication, division, exponentiation

### Example
Number: 1234
Possible solution: (1 * 2) * (3 * 4) = 24
Another solution: ((1 + 2) + 3) * 4 = 24
Another solution: (2 ^ 3) * (4 - 1) = 24
Another solution: (4 * 3) * (2 / 1) = 24
etc.

## Solver
This program is a solver for 24 that brute forces all possible results. It has three modes
depending on which lines you decomment.

### Mode 1
Get the number of solutions for all possible puzzles

### Mode 2
Challenge yourself by getting a puzzle with a solution which you have to solve (in a
properly parenthesized format)

### Mode 3
Get all the solutions for a single 4-digit number
