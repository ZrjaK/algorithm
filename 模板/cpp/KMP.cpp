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

vector<int> z_function(string s) {
  int n = (int)s.length();
  vector<int> z(n);
  for (int i = 1, l = 0, r = 0; i < n; ++i) {
    if (i <= r && z[i - l] < r - i + 1) {
      z[i] = z[i - l];
    } else {
      z[i] = max(0, r - i + 1);
      while (i + z[i] < n && s[z[i]] == s[i + z[i]]) ++z[i];
    }
    if (i + z[i] - 1 > r) l = i, r = i + z[i] - 1;
  }
  return z;
}
