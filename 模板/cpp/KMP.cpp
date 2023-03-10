vector<int> prefix_function(string& s) {
  int n = (int)s.length();
  vector<int> pi(n);
  for (int i = 1; i < n; i++) {
    int j = pi[i - 1];
    while (j > 0 && s[i] != s[j]) j = pi[j - 1];
    if (s[i] == s[j]) j++;
    pi[i] = j;
  }
  return pi;
}

vector<vector<int>> kmp_automaton(string& s) {
    int n = s.size();
    vector<vector<int>> nxt(n+1, vector<int>(26));
    for (int i = 1, j = 0; i <= n; i++) {
        j = nxt[j][s[i-1] - 'a'];
        nxt[i-1][s[i-1] - 'a'] = i;
        nxt[i] = vector<int>(nxt[j].begin(), nxt[j].end());
    }
    return nxt;
}