'''Solves the 24 game'''


# Operations allowed in the game
OPS = [lambda a, b: a + b,
       lambda a, b: a - b,
       lambda a, b: a * b,
       lambda a, b: a // b if a % b == 0 else None, # ignore cases where not divisible
       lambda a, b: a ** b if a in [0, 1] or b < 9 else None] # ignore exp > 9, won't get to 24
OP_NAMES = ['+', '-', '*', '/', '^']


def solve24(num):
    '''Returns solution strings corresponding to the 24 game via brute force'''
    digits = [num // 1000, (num // 100) % 10, (num // 10) % 10, num % 10]
    solutions = set()

    for a in range(4):
        for b in range(4):
            # Cannot reuse a number
            if a == b:
                continue

            # Get other two numbers
            c, d = set(range(4)) - set([a, b])

            for c, d in [(c, d), (d, c)]:
                for op1, opn1 in zip(OPS, OP_NAMES):
                    for op2, opn2 in zip(OPS, OP_NAMES):
                        for op3, opn3 in zip(OPS, OP_NAMES):
                            # Expression type (a op b) op (c op d)
                            try:
                                if op2(op1(digits[a], digits[b]), op3(digits[c], digits[d])) == 24:
                                    sol_str = '(%d %s %d) %s (%d %s %d)'
                                    sol_str = sol_str % (digits[a], opn1, digits[b],
                                                        opn2, digits[c], opn3, digits[d])
                                    solutions.add(sol_str)
                            except (TypeError, ZeroDivisionError, OverflowError):
                                pass
                            # Expression type ((a op b) op c) op d
                            try:
                                if op3(op2(op1(digits[a], digits[b]), digits[c]), digits[d]) == 24:
                                    sol_str = '((%d %s %d) %s %d) %s %d'
                                    sol_str = sol_str % (digits[a], opn1, digits[b],
                                                        opn2, digits[c], opn3, digits[d])
                                    solutions.add(sol_str)
                            except (TypeError, ZeroDivisionError, OverflowError):
                                pass
                            # Expression type (a op (b op c)) op d
                            try:
                                if op3(op1(digits[a], op2(digits[b], digits[c])), digits[d]) == 24:
                                    sol_str = '(%d %s (%d %s %d)) %s %d'
                                    sol_str = sol_str % (digits[a], opn1, digits[b],
                                                        opn2, digits[c], opn3, digits[d])
                                    solutions.add(sol_str)
                            except (TypeError, ZeroDivisionError, OverflowError):
                                pass
                            # Expression type a op ((b op c) op d)
                            try:
                                if op1(op3(digits[a], digits[b], op2(digits[c], digits[d]))) == 24:
                                    sol_str = '%d %s ((%d %s %d) %s %d)'
                                    sol_str = sol_str % (digits[a], opn1, digits[b],
                                                        opn2, digits[c], opn3, digits[d])
                                    solutions.add(sol_str)
                            except (TypeError, ZeroDivisionError, OverflowError):
                                pass
                            # Expression type a op (b op (c op d))
                            try:
                                if op1(digits[a], op2(digits[b], op3(digits[c], digits[d]))) == 24:
                                    sol_str = '%d %s (%d %s (%d %s %d))'
                                    sol_str = sol_str % (digits[a], opn1, digits[b],
                                                        opn2, digits[c], opn3, digits[d])
                                    solutions.add(sol_str)
                            except (TypeError, ZeroDivisionError, OverflowError):
                                pass

    # Return solutions found
    return solutions


# Run solver on 1234
if __name__ == '__main__':
    # Get number of solutions for all puzzles
    # UNCOMMENT LINES BELOW

    # for i in range(10000):
    #    print i, len(solve24(i))

    # Puzzle game
    # UNCOMMENT LINES BELOW

    from random import randint
    while (True):
        num = randint(0, 9999)
        sols = solve24(num)
        if len(sols) == 0:
            continue
        else:
            print(num)
        input_str = input()
        if input_str in sols:
            print("Correct!")
        else:
            print("Solution not found")
            print("Solutions:")
            for sol in solve24(num):
                print(sol)


    # Solve puzzle for arbitrary number
    # UNCOMMENT LINES BELOW

    # for sol in solve24(1234):
    #     print sol

    # Which digit is most commonly found in solutions?
    # UNCOMMENT LINES BELOW

    # d = {i: 0 for i in range(10)}

    # for i in range(10000):
    #     if i % 10 == 0:
    #         print(i)
    #     sol = ' '.join(solve24(i))
    #     for j in range(10):
    #         if str(j) in sol:
    #             d[j] += 1

    # print(d)
