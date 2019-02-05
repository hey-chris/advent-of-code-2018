state = "#.####...##..#....#####.##.......##.#..###.#####.###.##.###.###.#...#...##.#.##.#...#..#.##..##.#.##"

rules = {
'.##..': '.',
'..##.': '#',
'.#..#': '#',
'.#.#.': '.',
'..#..': '#',
'###..': '#',
'##..#': '.',
'##...': '#',
'#.###': '#',
'.##.#': '#',
'#....': '.',
'###.#': '.',
'.....': '.',
'.#...': '#',
'....#': '.',
'#.#..': '.',
'...#.': '#',
'#...#': '.',
'##.#.': '.',
'.#.##': '#',
'..#.#': '#',
'#.#.#': '.',
'.####': '.',
'#####': '.',
'..###': '.',
'...##': '.',
'#..##': '.',
'#.##.': '.',
'#..#.': '#',
'.###.': '#',
'##.##': '#',
'####.:, '.'
}


def parse_state(state):
    s = list(state)
    s0 = s.pop(0)
    s1 = s.pop(0)
    s += [s0, s1]
    return s


s = parse_state(state)
states = []
states.append(s)
for t in range(20):
    for i in range(len(s)):
        k = ''.join(s[i - 2: i + 2])
        try:
            v = rules[k]
            s[i] = v
        except KeyError:
            print('Key doesn\'t match the rules.')
        states.append(s)


summed = 0
for i in range(len(states[-1])):
    if states[-1][i] == '#':
        summed += i