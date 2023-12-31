from dataclasses import dataclass

ALIVE_SYMBOL = "☻"
DEAD_SYMBOL = "☺"
@dataclass
class LifeGrid:
    alive_cells: set[tuple[int, int]]

    def __init__(self):
        self.alive_cells = {(2, 1), (2, 2), (2, 3)}

    def evolve(self):
        neighbors_offset = (
            (-1, -1),  # Above left
            (-1, 0),  # Above
            (-1, 1),  # Above right
            (0, -1),  # Left
            (0, 1),  # Right
            (1, -1),  # Below left
            (1, 0),  # Below
            (1, 1),  # Below right
        )
        cells = {}
        for x, y in self.alive_cells:
            if (x, y) not in cells:
                cells[(x, y)] = 0

            for dx, dy in neighbors_offset:
                cells[(x + dx, y + dy)] = cells.get((x + dx, y + dy), 0) + 1

        alive_cells = set()
        for (x, y), value in cells.items():
            alive = (x, y) in self.alive_cells
            if alive:
                if 3 >= value >= 2:
                    alive_cells.add((x, y))
            else: # Dead cell
                if value == 3:
                    alive_cells.add((x, y))

        self.alive_cells = alive_cells

    def get_string_array(self, bounding_box):
        start_x, start_y, end_x, end_y = bounding_box

        display = []
        for x in range(start_x, end_x):
            row = []
            for y in range(start_y, end_y):
                symbol = ALIVE_SYMBOL if (x, y) in self.alive_cells else DEAD_SYMBOL
                row.append(symbol)

            display.append(row)

        
        return display

    def __str__(self):
        return (
            f"Alive Cells: {sorted(self.alive_cells)}"
        )
