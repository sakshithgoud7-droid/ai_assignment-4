from itertools import permutations

letters = ['T', 'W', 'O', 'F', 'U', 'R']
digits = range(10)

for perm in permutations(digits, len(letters)):
    T, W, O, F, U, R = perm
    if T == 0 or F == 0:
        continue

    TWO = 100*T + 10*W + O
    FOUR = 1000*F + 100*O + 10*U + R

    if TWO + TWO == FOUR:
        print("Solution found:")
        print(f"T={T}, W={W}, O={O}, F={F}, U={U}, R={R}")
        print(f"{TWO} + {TWO} = {FOUR}")
        break
