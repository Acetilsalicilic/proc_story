from simulation.world.terrain.terrain import Terrain

def get_terrain_str_repr(cell_grid: Terrain) -> list[str]:
    lines = list()

    for row in range(cell_grid.size_x):
        lines.append(list())
        for col in range(cell_grid.size_y):
            # represent this as symbols
            symbol = ''
            if cell_grid.cells[row][col].humidity == 1:
                symbol = '.'
            else:
                symbol = '#'

            lines[-1].append(f'{symbol} ')
    
    return lines

def print_to_stdout(lines: list[str]):
    for line in lines:
        line_str = ''
        for sym in line:
            line_str += sym
        print(line_str)