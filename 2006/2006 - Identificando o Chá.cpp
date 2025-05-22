#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(nullptr);
    
    int T, N, r = 0;
    
    cin >> T;
    
    for (int i = 0; i < 5; i++) {
        cin >> N;
        if (N == T) r++;
    }
    
    cout << r << endl;
    
    return 0;
}
