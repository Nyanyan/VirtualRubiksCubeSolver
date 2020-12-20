from basic_functions import *

def idxes_init(phase, cp, co, ep, eo):
    if phase == 0:
        res1 = co2idx(co)
        res2 = eo2idx(eo)
        res3 = ep2idx_phase0(ep)
        return (res1, res2, res3)
    else:
        res1 = cp2idx(cp)
        res2 = ep2idx_phase1_1(ep)
        res3 = ep2idx_phase1_2(ep)
        return (res1, res2, res3)

def trans(phase, idxes, twist):
    if phase == 0:
        res1 = trans_co[idxes[0]][twist]
        res2 = trans_eo[idxes[1]][twist]
        res3 = trans_ep_phase0[idxes[2]][twist]
        return (res1, res2, res3)
    else:
        res1 = idxes[0]
        for _ in range(loop[phase][twist]):
            res1 = trans_cp[res1][twist]
        res2 = trans_ep_phase1_1[idxes[1]][twist]
        res3 = trans_ep_phase1_2[idxes[2]][twist]
        return (res1, res2, res3)

def distance(phase, idxes):
    if phase == 0:
        return max(prun_phase0_co_ep[idxes[2]][idxes[0]], prun_phase0_eo_ep[idxes[2]][idxes[1]])
    else:
        return max(prun_phase1_cp_ep[idxes[2]][idxes[0]], prun_phase1_ep_ep[idxes[2]][idxes[1]])

def phase_search(phase, idxes, depth, dis):
    global phase_solution
    if depth == 0:
        return dis == 0
    depth -= 1
    for twist in range(12):
        n_idxes = trans(phase, idxes, twist)
        n_dis = distance(phase, n_idxes)
        if n_dis > dis or n_dis > depth:
            continue
        phase_solution.append(twist)
        if phase_search(phase, n_idxes, depth, n_dis):
            return True
        phase_solution.pop()
    return False

def solver(stickers):
    global phase_solution
    res = []
    cp, co, ep, eo = sticker2arr(stickers)
    for phase in range(2):
        idxes = idxes_init(phase, cp, co, ep, eo)
        dis = distance(phase, idxes)
        phase_solution = []
        for depth in range(dis, 20):
            print(phase, depth)
            if phase_search(phase, idxes, depth, dis):
                break
        else:
            return [-1]
        for twist in phase_solution:
            for _ in range(loop[phase][twist]):
                cp = move_cp(cp, twist)
                co = move_co(co, twist)
                ep = move_ep(ep, twist)
                eo = move_eo(eo, twist)
                res.append(twist)
    return res

trans_co = []
with open('trans_co.csv', mode='r') as f:
    for line in map(str.strip, f):
        trans_co.append([int(i) for i in line.replace('\n', '').split(',')])
trans_cp = []
with open('trans_cp.csv', mode='r') as f:
    for line in map(str.strip, f):
        trans_cp.append([int(i) for i in line.replace('\n', '').split(',')])
trans_eo = []
with open('trans_eo.csv', mode='r') as f:
    for line in map(str.strip, f):
        trans_eo.append([int(i) for i in line.replace('\n', '').split(',')])
trans_ep_phase0 = []
with open('trans_ep_phase0.csv', mode='r') as f:
    for line in map(str.strip, f):
        trans_ep_phase0.append([int(i) for i in line.replace('\n', '').split(',')])
trans_ep_phase1_1 = []
with open('trans_ep_phase1_1.csv', mode='r') as f:
    for line in map(str.strip, f):
        trans_ep_phase1_1.append([int(i) for i in line.replace('\n', '').split(',')])
trans_ep_phase1_2 = []
with open('trans_ep_phase1_2.csv', mode='r') as f:
    for line in map(str.strip, f):
        trans_ep_phase1_2.append([int(i) for i in line.replace('\n', '').split(',')])
prun_phase0_co_ep = []
with open('prun_phase0_co_ep.csv', mode='r') as f:
    for line in map(str.strip, f):
        prun_phase0_co_ep.append([int(i) for i in line.replace('\n', '').split(',')])
prun_phase0_eo_ep = []
with open('prun_phase0_eo_ep.csv', mode='r') as f:
    for line in map(str.strip, f):
        prun_phase0_eo_ep.append([int(i) for i in line.replace('\n', '').split(',')])
prun_phase1_cp_ep = []
with open('prun_phase1_cp_ep.csv', mode='r') as f:
    for line in map(str.strip, f):
        prun_phase1_cp_ep.append([int(i) for i in line.replace('\n', '').split(',')])
prun_phase1_ep_ep = []
with open('prun_phase1_ep_ep.csv', mode='r') as f:
    for line in map(str.strip, f):
        prun_phase1_ep_ep.append([int(i) for i in line.replace('\n', '').split(',')])
print('initialize done')
phase_solution = []

#stickers = [0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 5, 1, 1, 5, 1, 1, 5, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 3, 3, 0, 3, 3, 0, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 3, 5, 5, 3, 5, 5, 3]
#print(solver(stickers))