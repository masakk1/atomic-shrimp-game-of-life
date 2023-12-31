# Credits
The original: Conway's game of life:
[wikipedia page](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)

Atomic Shrimp's Video:
[youtube video](https://www.youtube.com/watch?v=hwt6P425Fjc)

# Atomic Shrimp's Idea
1. Using letters of the alphabet instead of blocks
2. Instead of Life & Dead, change state of the letter
    - General relationships of vowels and consonants
    - Pairing "Q" and "U"
    - Frequency of letters occuring in English (or other language)
3. Tune the weights on purpose
4. See what happens
5. ???
5. PROFIT

# Guide

## Game of Life
### TODO
1. [ ] Implement the Game of Life algorithm, including the life grid and the seeds or patterns
2. [ ] Provide a way to visualize the life grid and its evolution
3. [ ] Allow the user to set a pattern and run the game a given number of generations

### Rules
1. Alive cells die if they have fewer than two (underpopulation) or more than three living neighbors (overpopulation).
2. Alive cells stay alive if they have two or three living neighbors.
3. Dead cells with exactly three living neighbors become alive (reproduction).