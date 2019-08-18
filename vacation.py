# https://codeforces.com/problemset/problem/698/A
n = input()
inp = map(int, raw_input().split())


def greedy_best_choice(days):
    """Select best option in case of 3 when prev rested"""
    if len(days) == 0:
        return 1 # no effect or 1 or 2

    cur = days[0]
    if cur == 3:
        cur = greedy_best_choice(days[1:])

    if cur == 1:
        return 2
    elif cur == 2:
        return 1
    else:
        return 1


def greedy_lookup(days):
    """Strategy: Don't postpone to another day"""
    prev = 0 # 0: nothing, 1: contest, 2: Gim
    rest = 0

    for i, d in enumerate(days):
        if d == 0:
            rest += 1
            prev = 0
        elif d == 1:
            if prev == 1:
                rest += 1
                prev = 0
            else:
                prev = 1
        elif d == 2:
            if prev == 2:
                rest += 1
                prev = 0
            else:
                prev = 2
        elif d == 3:
            if prev == 1:
                prev = 2
            elif prev == 2:
                prev = 1
            elif prev == 0:
                prev = greedy_best_choice(days[i+1:])
        #print prev

    return rest

if __name__ == '__main__':
    rest = greedy_lookup(inp)
    print(rest)
