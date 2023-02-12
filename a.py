from itertools import permutations

print(6*5*4*3*2*1)
for lst in permutations(range(1, 7), 6):
    print(6)
    print(*lst)