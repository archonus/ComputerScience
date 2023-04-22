from collections import deque
import math


def find_preds(g, s, t):
    preds = {v: [] for v in g}
    distance = {v: math.inf for v in g}

    queue = deque([s])
    distance[s] = 0

    while queue:
        v = queue.pop()
        if v == t:
            break
        d = distance[v] + 1
        for w in g[v]: # Neighbours of v
            if math.isinf(distance[w]): # Unseen
                distance[w] = d
                queue.appendleft(w)
                preds[w].append(v)
            
            elif distance[w] == d: # An alternate paths
                preds[w].append(v)
    return preds


def shortest_paths(g,s,t):
    preds = find_preds(g,s,t)
    if len(preds[t]) == 0:
        return []
    def find_paths(t):
        if len(preds[t]) == 0: # Zero length path
            return [[t]]
        else:
            paths = []
            for pred in preds[t]:
                pred_paths = find_paths(pred)
                for pred_path in pred_paths:
                    paths.append(pred_path + [t])
            return paths
    return find_paths(t)

if __name__ == '__main__':
    g = {0: {3}, 1: {2, 3}, 2: set(), 3: {2}}
    p = shortest_paths(g,3,1)
    print(p)     



