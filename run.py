from golife import grid, patterns

blinker = patterns.Pattern(
    name="Blinker",
    alive_cells={(2, 1), (2, 2), (2, 3)},
)

grid = grid.LifeGrid(blinker)
print(grid)

for _ in range(10):
    grid.evolve()
    print(grid.as_string( (0, 0, 10, 10) ))