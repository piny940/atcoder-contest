import sys
import re

INVALID_INPUT = 'invalid input'
MIN_S_LEN = 1
MAX_S_LEN = 50
MIN_A = 1
MAX_A = 100
MIN_M = 1
MAX_M = 5
MIN_N = 1
MAX_N = 10000000
def main(lines):
    line = lines[0]
    if contains_control_chars(line):
        print(INVALID_INPUT)
        return
    splitted = line.split()
    if len(splitted) < 2:
        print(INVALID_INPUT)
        return
    n, pairs = parse_num(splitted[-1], MIN_N, MAX_N), parse_pairs(' '.join(splitted[:-1]))
    if n is None or pairs is None:
        print(INVALID_INPUT)
        return
    
    # Sort by a[i]
    pairs.sort(key=lambda pair: pair[0], reverse=True)
    
    for a, s in pairs:
        if n % a == 0:
            print(s)
            return
    print(n)

def contains_control_chars(s: str):
    re.match(r'[\x00-\x1F\x7F]', s)

def parse_num(n_str: str, min: int, max: int):
    try:
        if n_str.startswith('0'):
            return None
        n = int(n_str)
        if n < min or n > max:
            return None
        return n
    except ValueError:
        return None

def parse_pair(pair_str: str):
    splitted = pair_str.split(':')
    if len(splitted) != 2:
        return None, None
    a_str, s = splitted
    a = parse_num(a_str, MIN_A, MAX_A)
    if a is None:
        return None, None
    if len(s) < MIN_S_LEN or len(s) > MAX_S_LEN:
        return None, None
    return (a, s)

def parse_pairs(pairs_str: str):
    splitted = pairs_str.split()
    if len(splitted) < MIN_M or len(splitted) > MAX_M:
        return None
    pairs = []
    for pair_str in splitted:
        a, s = parse_pair(pair_str)
        if a is None or s is None:
            return None
        pairs.append((a, s))

    # Check is a[i] is unique
    arr = [a for a, _ in pairs]
    if len(arr) != len(set(arr)):
        return None

    return pairs


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
