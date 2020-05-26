from itertools import permutations

def print_perm(n):
    array = list(range(1, n+1))
    perm = permutations(array)
    perm_all_in_1d_array = []
    for p in list(perm):
        for i in p:
            perm_all_in_1d_array.append(i)
    print(perm_all_in_1d_array)

print_perm(4)
