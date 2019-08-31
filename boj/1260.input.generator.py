import random
import sys

max_number_of_vertices = 1000
max_number_of_edges = 10000

# Overwrite for small sample
if len(sys.argv) == 2:
    max_number_of_vertices = int(sys.argv[1])
    max_number_of_edges = max_number_of_vertices * 2
elif len(sys.argv) == 3:
    max_number_of_vertices = int(sys.argv[1])
    max_number_of_edges = int(sys.argv[2])

number_of_vertices = random.randint(2, max_number_of_vertices)
number_of_edges = random.randint(1, max_number_of_edges)
starting_vertex = random.randint(1, number_of_vertices)

print(f'{number_of_vertices} {number_of_edges} {starting_vertex}')
for _ in range(number_of_edges):
    v1 = random.randint(1, number_of_vertices)
    v2 = random.randint(1, number_of_vertices-1)

    if v2 >= v1:
        v2 += 1

    print(f'{v1} {v2}')
