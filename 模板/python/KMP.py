def prefix_function(s):
    n = len(s)
    pi = [0] * n
    for i in range(1, n):
        j = pi[i - 1]
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j
    return pi

def kmp_automaton(s):
    n = len(s)
    s = [ord(i) - 97 for i in s]
    nxt = [[0] * 26 for _ in range(n+1)]
    j = 0
    for i in range(1, n+1):
        j = nxt[j][s[i-1]]
        nxt[i-1][s[i-1]] = i
        nxt[i] = deepcopy(nxt[j])
    return nxt