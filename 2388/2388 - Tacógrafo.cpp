#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(nullptr);
    
    int n = 0;
    int s = 0;
    
    cin >> n;
    int t[n], v[n];
    
    for(int i = 0; i < n; i++) {
        cin >> t[i] >> v[i];
        s += t[i] * v[i];
    }
    cout << s << "\n";

    return 0;
}
