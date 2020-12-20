'''
corner numbering
  0 1
   U
0 3 2 1
 L F R
7 4 5 6
   D
  7 6

edge numbering
       0
     3 U 1
       2
11 L 8 F 9 R 10
       4
     7 D 5
       6

sticker numbering
              U
           0  1  2
           3  4  5
           6  7  8
    L         F         R         B
36 37 38   9 10 11  18 19 20  27 28 29
39 40 41  12 13 14  21 22 23  30 31 32
42 43 44  15 16 17  24 25 26  33 34 35
              D
          45 46 47
          48 49 50
          51 52 53

color numbering
white: 0
green: 1
red: 2
blue: 3
orange: 4
yellow: 5

'''


#              0    1    2    3    4    5    6    7    8    9    10   11
#              R    R'   L    L'   U    U'   D    D'   F    F'   B    B'
twists_key = ['i', 'k', 'd', 'e', 'j', 'f', 's', 'l', 'h', 'g', 'w', 'o']
loop = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2]]

corner_places = [(0, 36, 29), (2, 27, 20), (8, 18, 11), (6, 9, 38), (45, 44, 15), (47, 17, 24), (53, 26, 33), (51, 35, 42)]
corner_colors = [(0, 4, 3),   (0, 3, 2),   (0, 2, 1),   (0, 1, 4),  (5, 4, 1),    (5, 1, 2),    (5, 2, 3),    (5, 3, 4)   ]
edge_places = [(1, 28), (5, 19), (7, 10), (3, 37), (46, 16), (50, 25), (52, 34), (48, 43), (12, 41), (14, 21), (30, 23), (32, 39)]
edge_colors = [(0, 3),  (0, 2),  (0, 1),  (0, 4),  (5, 1),   (5, 2),   (5, 3),   (5, 4),   (1, 4),   (1, 2),   (3, 2),   (3, 4)  ]

fac = [1]
for i in range(1, 13):
    fac.append(fac[-1] * i)

corner_move_parts = [
    (1, 6, 5, 2), # R
    (3, 4, 0, 7), # L
    (0, 1, 2, 3), # U
    (4, 5, 6, 7), # D
    (2, 5, 3, 4), # F
    (0, 7, 6, 1)  # B
]
co_plus = (1, 2, 1, 2)
edge_move_parts = [
    (1, 10, 5, 9), # R
    (3, 8, 7, 11), # L
    (0, 1, 2, 3),  # U
    (4, 5, 6, 7),  # D
    (2, 9, 4, 8),  # F
    (0, 11, 6, 10) # B
]

def sticker2arr(stickers):
    cp = [-1 for _ in range(8)]
    co = [-1 for _ in range(8)]
    for place in range(8):
        part_color = [stickers[i] for i in corner_places[place]]
        for part in range(8):
            for dr in range(3):
                for sticker in range(3):
                    if part_color[sticker] != corner_colors[part][(sticker - dr) % 3]:
                        break
                else:
                    cp[place] = part
                    co[place] = dr
                    break
            else:
                continue
            break
    ep = [-1 for _ in range(12)]
    eo = [-1 for _ in range(12)]
    for place in range(12):
        part_color = [stickers[i] for i in edge_places[place]]
        for part in range(12):
            for dr in range(2):
                for sticker in range(2):
                    if part_color[sticker] != edge_colors[part][(sticker - dr) % 2]:
                        break
                else:
                    ep[place] = part
                    eo[place] = dr
                    break
            else:
                continue
            break
    return cp, co, ep, eo

def move_cp(cp, twist):
    twist_type = twist // 2
    twist_amount = 3 if twist % 2 else 1
    res = [i for i in cp]
    for _ in range(twist_amount):
        n_res = [i for i in res]
        for i in range(4):
            n_res[corner_move_parts[twist_type][(i + 1) % 4]] = res[corner_move_parts[twist_type][i]]
        res = n_res
    return res

def move_co(co, twist):
    twist_type = twist // 2
    twist_amount = 3 if twist % 2 else 1
    res = [i for i in co]
    flip_flag = twist_type != 2 and twist_type != 3
    for _ in range(twist_amount):
        n_res = [i for i in res]
        for i in range(4):
            n_res[corner_move_parts[twist_type][(i + 1) % 4]] = res[corner_move_parts[twist_type][i]]
            if flip_flag:
                n_res[corner_move_parts[twist_type][(i + 1) % 4]] += co_plus[(i + 1) % 4]
                n_res[corner_move_parts[twist_type][(i + 1) % 4]] %= 3
        res = n_res
    return res

def move_ep(ep, twist):
    twist_type = twist // 2
    twist_amount = 3 if twist % 2 else 1
    res = [i for i in ep]
    for _ in range(twist_amount):
        n_res = [i for i in res]
        for i in range(4):
            n_res[edge_move_parts[twist_type][(i + 1) % 4]] = res[edge_move_parts[twist_type][i]]
        res = n_res
    return res

def move_eo(eo, twist):
    twist_type = twist // 2
    twist_amount = 3 if twist % 2 else 1
    res = [i for i in eo]
    flip_flag = int(twist_type == 4 or twist_type == 5)
    for _ in range(twist_amount):
        n_res = [i for i in res]
        for i in range(4):
            n_res[edge_move_parts[twist_type][(i + 1) % 4]] = res[edge_move_parts[twist_type][i]]
            if flip_flag:
                n_res[edge_move_parts[twist_type][(i + 1) % 4]] = 1 - n_res[edge_move_parts[twist_type][(i + 1) % 4]]
        res = n_res
    return res

def cmb(n, r):
    return fac[n] // fac[r] // fac[n - r]

def cp2idx(cp):
    res = 0
    for i in range(8):
        cnt = cp[i]
        for j in cp[:i]:
            if j < cp[i]:
                cnt -= 1
        res += fac[7 - i] * cnt
    return res

def idx2cp(idx):
    res = [-1 for _ in range(8)]
    for i in range(8):
        candidate = idx // fac[7 - i]
        marked = [True for _ in range(i)]
        for _ in range(8):
            for j, k in enumerate(res[:i]):
                if k <= candidate and marked[j]:
                    candidate += 1
                    marked[j] = False
        res[i] = candidate
        idx %= fac[7 - i]
    return res

def co2idx(co):
    res = 0
    for i in range(7):
        res *= 3
        res += co[i]
    return res

def idx2co(idx):
    res = [-1 for _ in range(8)]
    for i in range(7):
        res[6 - i] = idx % 3
        idx //= 3
    res[7] = (3 - sum(res) % 3) % 3
    return res

def ep2idx_phase0(ep):
    res = 0
    cnt = 4
    for i in reversed(range(12)):
        if ep[i] >= 8:
            res += cmb(i, cnt)
            cnt -= 1
    return res

def idx2ep_phase0(idx):
    res = [-1 for _ in range(12)]
    cnt = 4
    for i in reversed(range(12)):
        c = cmb(i, cnt)
        if idx >= c:
            res[i] = 8
            idx -= c
            cnt -= 1
    return res

def ep2idx_phase1_1(ep):
    res = 0
    for i in range(8):
        cnt = ep[i]
        for j in ep[:i]:
            if j < ep[i]:
                cnt -= 1
        res += fac[7 - i] * cnt
    return res

def ep2idx_phase1_2(ep):
    res = 0
    for i in range(4):
        cnt = ep[8 + i] - 8
        for j in ep[8:8 + i]:
            if j < ep[8 + i]:
                cnt -= 1
        res += fac[3 - i] * cnt
    return res

def idx2ep_phase1_1(idx1):
    res = [-1 for _ in range(12)]
    for i in range(8):
        candidate = idx1 // fac[7 - i]
        marked = [True for _ in range(i)]
        for _ in range(8):
            for j, k in enumerate(res[:i]):
                if k <= candidate and marked[j]:
                    candidate += 1
                    marked[j] = False
        res[i] = candidate
        idx1 %= fac[7 - i]
    return res

def idx2ep_phase1_2(idx2):
    res = [-1 for _ in range(12)]
    for i in range(4):
        candidate = idx2 // fac[3 - i]
        marked = [True for _ in range(i)]
        for _ in range(4):
            for j, k in enumerate(res[8:8 + i]):
                if k <= candidate and marked[j]:
                    candidate += 1
                    marked[j] = False
        res[8 + i] = candidate
        idx2 %= fac[3 - i]
    for i in range(4):
        res[8 + i] += 8
    return res

def eo2idx(eo):
    res = 0
    for i in eo[:11]:
        res *= 2
        res += i
    return res

def idx2eo(idx):
    res = [0 for _ in range(12)]
    for i in reversed(range(11)):
        res[i] = idx % 2
        idx //= 2
    res[11] = sum(res) % 2
    return res