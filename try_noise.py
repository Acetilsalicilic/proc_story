import sys
from noise import pnoise2

file = sys.argv[1]
seed = int(sys.argv[2])

size_x = int(sys.argv[3])
size_y = int(sys.argv[4])

frequency = float(sys.argv[5])

# open the file
with open(file, 'w') as file:
    # rows
    for y_index in range(size_y):
        # cols
        for x_index in range(size_x):
            file.write(f'{pnoise2(x_index / frequency, y_index / frequency, base=seed):.2f}\t')
        
        file.write('\n')

print('Done!')