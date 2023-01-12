def EulerTour(n, edges, root=0):
    L = [-1] * n
    R = [0] * n
    stack = [(root, 1), (root, 0)]
    ind = 0
    while stack:
        pos, t = stack.pop()
        if t == 0:
            L[pos] = ind
            ind += 1
            for npos in edges[pos]:
                if L[npos] != -1:
                    continue
                stack.append((npos, 1))
                stack.append((npos, 0))
        else:
            R[pos] = ind
 
    return L, R