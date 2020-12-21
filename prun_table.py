from basic_functions import *
import csv
from collections import deque

inf = 1000

def table_phase0():
    trans_ep = []
    with open('trans_ep_phase0.csv', mode='r') as f:
        for line in map(str.strip, f):
            trans_ep.append([int(i) for i in line.replace('\n', '').split(',')])

    trans = []
    with open('trans_co.csv', mode='r') as f:
        for line in map(str.strip, f):
            trans.append([int(i) for i in line.replace('\n', '').split(',')])
    table = [[inf for _ in range(2187)] for _ in range(495)]
    solved1 = ep2idx_phase0(list(range(12)))
    solved2 = co2idx([0 for _ in range(8)])
    que = deque([[solved1, solved2, 0]])
    table[solved1][solved2] = 0
    cnt = 0
    while que:
        idx1, idx2, cost = que.popleft()
        cost += 1
        for twist_idx, twist in enumerate(candidate[0]):
            n_idx1 = trans_ep[idx1][twist_idx]
            n_idx2 = trans[idx2][twist_idx]
            if table[n_idx1][n_idx2] > cost:
                table[n_idx1][n_idx2] = cost
                que.append([n_idx1, n_idx2, cost])
    with open('prun_phase0_co_ep.csv', mode='w') as f:
        writer = csv.writer(f, lineterminator='\n')
        for arr in table:
            writer.writerow(arr)

    trans = []
    with open('trans_eo.csv', mode='r') as f:
        for line in map(str.strip, f):
            trans.append([int(i) for i in line.replace('\n', '').split(',')])
    table = [[inf for _ in range(2048)] for _ in range(495)]
    solved1 = ep2idx_phase0(list(range(12)))
    solved2 = eo2idx([0 for _ in range(12)])
    que = deque([[solved1, solved2, 0]])
    table[solved1][solved2] = 0
    while que:
        idx1, idx2, cost = que.popleft()
        cost += 1
        for twist_idx, twist in enumerate(candidate[0]):
            n_idx1 = trans_ep[idx1][twist_idx]
            n_idx2 = trans[idx2][twist_idx]
            if table[n_idx1][n_idx2] > cost:
                table[n_idx1][n_idx2] = cost
                que.append([n_idx1, n_idx2, cost])
    with open('prun_phase0_eo_ep.csv', mode='w') as f:
        writer = csv.writer(f, lineterminator='\n')
        for arr in table:
            writer.writerow(arr)


def table_phase1():
    trans_ep = []
    with open('trans_ep_phase1_2.csv', mode='r') as f:
        for line in map(str.strip, f):
            trans_ep.append([int(i) for i in line.replace('\n', '').split(',')])
    trans = []
    with open('trans_cp.csv', mode='r') as f:
        for line in map(str.strip, f):
            trans.append([int(i) for i in line.replace('\n', '').split(',')])
    table = [[inf for _ in range(40320)] for _ in range(24)]
    solved1 = ep2idx_phase1_2(list(range(12)))
    solved2 = cp2idx(list(range(8)))
    table[solved1][solved2]  = 0
    que = deque([[solved1, solved2, 0]])
    while que:
        idx1, idx2, cost = que.popleft()
        cost += 1
        for twist_idx, twist in enumerate(candidate[1]):
            n_idx1 = trans_ep[idx1][twist_idx]
            n_idx2 = trans[idx2][twist_idx]
            if table[n_idx1][n_idx2] > cost:
                table[n_idx1][n_idx2] = cost
                que.append([n_idx1, n_idx2, cost])
    with open('prun_phase1_cp_ep.csv', mode='w') as f:
        writer = csv.writer(f, lineterminator='\n')
        for arr in table:
            writer.writerow(arr)
    trans = []
    with open('trans_ep_phase1_1.csv', mode='r') as f:
        for line in map(str.strip, f):
            trans.append([int(i) for i in line.replace('\n', '').split(',')])
    table = [[inf for _ in range(40320)] for _ in range(24)]
    solved1 = ep2idx_phase1_2(list(range(12)))
    solved2 = ep2idx_phase1_1(list(range(12)))
    table[solved1][solved2]  = 0
    que = deque([[solved1, solved2, 0]])
    while que:
        idx1, idx2, cost = que.popleft()
        cost += 1
        for twist_idx, twist in enumerate(candidate[1]):
            n_idx1 = trans_ep[idx1][twist_idx]
            n_idx2 = trans[idx2][twist_idx]
            if table[n_idx1][n_idx2] > cost:
                table[n_idx1][n_idx2] = cost
                que.append([n_idx1, n_idx2, cost])
    with open('prun_phase1_ep_ep.csv', mode='w') as f:
        writer = csv.writer(f, lineterminator='\n')
        for arr in table:
            writer.writerow(arr)


table_phase0()
table_phase1()