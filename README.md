# Simple Chess AI with Minimax Algorithm

### Introduction

* This repo includes my solution of the given homework(1/2) in the scope of the Artifical Intelligence(CENG461) course which is given as a technical elective in 2019-2020 Fall semester by Computer Engineering Department at Izmir Institute of Technology.
    
* (*)README.md file uses some parts of the official Homework Doc to better express the purpose of the Homework. 

### Problem* 

* In this homework, you should code a program that plays chess. The UI is already coded for you, you are asked to code the program which takes a scenario (or
starting board) and calculates the best possible move. The program should play against the user, first AI makes the move then user and it goes like this.

### Approach*

* The chess game is based on making decision based on the current board at each step. So you should create a tree based on legal moves at each step, and expand the leaves based on legal moves at each leaf as well. Since this problem is exponentially complex to the number of possible moves, you are asked to search for until depth 5 (in other words, AI only thinks 5 move ahead like ”AI-user-AI-user-AI”). There is an algorithm called minimax, which you can use in your program, for search in turn-based decision systems. Also you need a value function to evaluate each moves and what parameters your function depends on is up to you.

### Example Scenarios*

* There are several notations to represent chess boards. In this homework, we use Forsyth-Edwards Notation (FEN). The links are given below to clarify what the characters of notation stands for:
        https://en.wikipedia.org/wiki/Forsyth%E2%80%93Edwards_Notation
        https://www.chessgames.com/fenhelp.html

* The 1 move ahead scenarios:
- Checkmating:
    8/5K1k/8/8/8/8/8/6Q1 w - - 0 1
    8/8/8/8/k7/8/1R3K2/1R6 w - - 0 1
    1Q6/8/8/2R3K1/8/8/8/k7 w - - 0 1

- Preventing from checkmate:
    6k1/r4Qpp/8/8/8/4K3/8/8 b - - 0 1
    2k2R2/1b1p4/3B2r1/8/4q3/6p1/ppp5/1k1r4 b - - 0 1

* The 3 move ahead of checkmating scenarios:
    3Q4/8/8/2R3K1/8/8/k7/8 w - - 0 1
    8/8/8/8/8/7k/4KR2/6R1 w - - 0 1
    3K2R1/n3r3/5P1P/8/n7/pp6/kp6/3Q4 b - - 0 1

### Implementation and Result Showcase

* The implementation of chess_ai.py file provided by me as a solution. This file includes neccessary functions. I implemented two version of minimax algorithm with functions names:
- minimax_ai_play(board, depth, maximizingPlayer)
- alpha_beta_minimax(board, depth, alpha, beta, maximizingPlayer)

* I have used below pseudocodes which can be found in (https://en.wikipedia.org/wiki/Minimax). The main purpose was to understand the core mechanism of the algorithms. Therefore implementations made far away from production readiness. In this aspect, I'm always open to feedback.

```
    function minimax(node, depth, maximizingPlayer) is
    if depth = 0 or node is a terminal node then
        return the heuristic value of node
    if maximizingPlayer then
        value := −∞
        for each child of node do
            value := max(value, minimax(child, depth − 1, FALSE))
        return value
    else (* minimizing player *)
        value := +∞
        for each child of node do
            value := min(value, minimax(child, depth − 1, TRUE))
        return value

    function alphabeta(node, depth, α, β, maximizingPlayer) is
    if depth = 0 or node is a terminal node then
        return the heuristic value of node
    if maximizingPlayer then
        value := −∞
        for each child of node do
            value := max(value, alphabeta(child, depth − 1, α, β, FALSE))
            α := max(α, value)
            if α ≥ β then
                break (* β cut-off *)
        return value
    else
        value := +∞
        for each child of node do
            value := min(value, alphabeta(child, depth − 1, α, β, TRUE))
            β := min(β, value)
            if α ≥ β then
                break (* α cut-off *)
        return value
```
